from pathlib import Path
from datetime import datetime

def generar_reporte(ruta: Path, plan: object, resultados: list, backup: str, estado: str, errores: list = None):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    errores = errores or []
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(f"# Reporte de cambios\n\n")
        f.write(f"## Estado final\n**{estado}**\n\n")
        f.write(f"## Documento base\n`{plan.documento_base if plan else 'N/A'}`\n\n")
        f.write(f"## Documento generado\n`{plan.documento_salida if plan else 'N/A'}`\n\n")
        f.write(f"## Backup\n`{backup}`\n\n")
        
        if resultados:
            f.write(f"## Cambios aplicados\n\n")
            f.write("| ID | Tipo | Referencia | Estado |\n|---|---|---|---|\n")
            for r in resultados:
                f.write(f"| {r['id']} | {r['tipo']} | {r['ref']} | {r['estado']} |\n")
        
        if errores:
            f.write(f"\n## Errores y Advertencias\n")
            for e in errores: f.write(f"- {e}\n")
            
        f.write(f"\n## Fecha de ejecución\n{fecha}\n")
