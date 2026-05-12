import argparse
import sys
from pathlib import Path
from datetime import datetime
from src.change_plan_parser import cargar_plan_desde_archivo, parsear_plan
from src.validator import validar_plan_completo
from src.markdown_loader import cargar_contenido, guardar_contenido
from src.backup_manager import crear_backup
from src.reporter import generar_reporte
from src.patch_engine import aplicar_parches, PatchBloqueado

def main():
    """
    Orquestador principal del MVP v1.1.
    Flujo de validación:
    1. Estática (validator.py): Antes de cargar archivos.
    2. Dinámica (patch_engine.py): Durante la aplicación, contra el contenido real.
    """
    parser = argparse.ArgumentParser(description="DocPatchManager: Aplicador seguro de parches Markdown.")
    parser.add_argument("--plan", required=True, help="Ruta al archivo JSON del plan de cambios.")
    args = parser.parse_args()
    
    root = Path.cwd()
    plan = None
    resultados = []
    backup = "N/A"
    
    try:
        # FASE 1: Carga del Plan
        ruta_p = root / args.plan
        plan_datos = cargar_plan_desde_archivo(ruta_p)
        plan = parsear_plan(plan_datos)
        
        # FASE 2: Validación Estática (Capa 1)
        # Valida V1, V2, V3, V10, V4, V5, V6, V7, V8
        # No requiere el contenido del documento base.
        errores = validar_plan_completo(plan, root)
        if errores:
            generar_reporte(root / "output/reportes/error_validacion.md", plan, [], "N/A", "PATCH_BLOQUEADO", errores)
            print("❌ PATCH_BLOQUEADO")
            for e in errores: print(f"  {e}")
            sys.exit(1)
            
        # FASE 3: Preparación (Carga de contenido y Backup)
        contenido = cargar_contenido(root / plan.documento_base)
        
        if plan.crear_backup:
            backup = str(crear_backup(root / plan.documento_base, root / "output/backups"))
            
        # FASE 4: Validación Dinámica y Aplicación (Capa 2)
        # Aquí se valida V9 (referencias únicas y existentes en el contenido).
        nuevo_contenido, resultados = aplicar_parches(contenido, plan.cambios)
        
        # FASE 5: Persistencia y Cierre
        guardar_contenido(root / plan.documento_salida, nuevo_contenido)
        
        if plan.generar_reporte:
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            generar_reporte(root / f"output/reportes/reporte_{ts}.md", plan, resultados, backup, "PATCH_APLICADO")
        print("✅ PATCH_APLICADO")
        
    except PatchBloqueado as e:
        print(f"❌ PATCH_BLOQUEADO: {e}")
        if plan:
            generar_reporte(root / "output/reportes/reporte_bloqueo.md", plan, resultados, backup, "PATCH_BLOQUEADO", [str(e)])
        sys.exit(1)
    except Exception as e:
        print(f"❌ PATCH_ERROR: {e}")
        if plan:
            generar_reporte(root / "output/reportes/reporte_error.md", plan, resultados, backup, "PATCH_ERROR", [str(e)])
        sys.exit(1)

if __name__ == "__main__":
    main()
