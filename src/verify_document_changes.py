import argparse
import sys
import os
from pathlib import Path
from datetime import datetime

# File: src/verify_document_changes.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Verificación analítica post-edición de documentos Markdown.
# Rol: Auditor determinista de integridad documental (v1.2.2).
# ──────────────────────────────────────────────────────────────────────

def leer_archivo(ruta):
    if not os.path.exists(ruta):
        return None
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return f.read()
    except (OSError, UnicodeDecodeError):
        return None

def extraer_encabezados(contenido):
    """Extrae líneas que comienzan con # (Markdown headers)."""
    if not contenido:
        return []
    return [line.strip() for line in contenido.splitlines() if line.strip().startswith('#')]

def contar_metricas(contenido):
    if not contenido:
        return 0, 0
    lineas = contenido.splitlines()
    palabras = contenido.split()
    return len(lineas), len(palabras)

def analizar_seguridad(m_antes, m_despues, h_antes, h_despues):
    warnings = []
    bloqueos = []
    
    l_antes, p_antes = m_antes
    l_despues, p_despues = m_despues
    
    # 1. Validaciones Críticas (BLOQUEOS)
    if l_despues == 0:
        bloqueos.append("El documento de salida está vacío.")
        
    set_antes = set(h_antes)
    set_despues = set(h_despues)
    eliminados = sorted(list(set_antes - set_despues))
    if eliminados:
        bloqueos.append(f"Se han eliminado encabezados: {', '.join(eliminados[:3])}...")
        
    if l_antes > 0:
        reduccion = (l_antes - l_despues) / l_antes
        if reduccion > 0.30:
            bloqueos.append(f"Reducción crítica de líneas (>30%): -{reduccion:.1%}")
        elif reduccion > 0.10:
            warnings.append(f"Reducción moderada de líneas (>10%): -{reduccion:.1%}")
            
        crecimiento = (l_despues - l_antes) / l_antes
        if crecimiento > 0.30:
            warnings.append(f"Crecimiento alto de líneas (>30%): +{crecimiento:.1%}")

    # 2. Validaciones de Advertencia (WARNINGS)
    duplicados = sorted([h for h in set_despues if h_despues.count(h) > 1])
    if duplicados:
        warnings.append(f"Encabezados duplicados detectados: {', '.join(duplicados[:3])}...")

    if bloqueos:
        return "VERIFY_BLOCKED", bloqueos, warnings
    if warnings:
        return "VERIFY_WARNING", bloqueos, warnings
    return "VERIFY_OK", [], []

def generar_reporte_markdown(estado, b_path, a_path, m_antes, m_despues, h_antes, h_despues, bloqueos, warnings):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Pre-calculo de cadenas para evitar lógica compleja en f-strings (Python < 3.12 compatibility)
    h_nuevos = sorted(list(set(h_despues) - set(h_antes)))
    h_eliminados = sorted(list(set(h_antes) - set(h_despues)))
    h_duplicados = sorted([h for h in set(h_despues) if h_despues.count(h) > 1])
    
    str_nuevos = "\n".join(["- " + h for h in h_nuevos]) if h_nuevos else "- Ninguno"
    str_eliminados = "\n".join(["- " + h for h in h_eliminados]) if h_eliminados else "- Ninguno"
    str_duplicados = "\n".join(["- " + h for h in h_duplicados]) if h_duplicados else "- Ninguno"
    
    str_bloqueos = "\n".join(["- ❌ " + b for b in bloqueos]) if bloqueos else ""
    str_warnings = "\n".join(["- ⚠️ " + w for w in warnings]) if warnings else ""
    str_limpio = "- Ninguna" if not bloqueos and not warnings else ""
    
    l_diff = m_despues[0] - m_antes[0]
    p_diff = m_despues[1] - m_antes[1]

    report = f"""# Verificación documental

## Estado final

**{estado}**

## Archivos comparados

- **Before:** `{b_path}`
- **After:** `{a_path}`

## Métricas

| Métrica | Antes | Después | Diferencia |
|---|---:|---:|---:|
| Líneas | {m_antes[0]} | {m_despues[0]} | {l_diff:+} |
| Palabras | {m_antes[1]} | {m_despues[1]} | {p_diff:+} |

## Encabezados nuevos
{str_nuevos}

## Encabezados eliminados
{str_eliminados}

## Encabezados duplicados
{str_duplicados}

## Advertencias / Bloqueos
{str_bloqueos}
{str_warnings}
{str_limpio}

## Fecha de ejecución
{ts}
"""
    return report

def main():
    parser = argparse.ArgumentParser(description="Verificador de integridad documental.")
    parser.add_argument("--before", required=True)
    parser.add_argument("--after", required=True)
    parser.add_argument("--report", help="Ruta para guardar el reporte Markdown.")
    args = parser.parse_args()

    c_antes = leer_archivo(args.before)
    c_despues = leer_archivo(args.after)

    # Si hay fallo de lectura, gestionamos el reporte de error
    if c_antes is None or c_despues is None:
        estado = "VERIFY_BLOCKED"
        bloqueos = ["No se pudo leer o encontrar alguno de los archivos de entrada."]
        if args.report:
            reporte_error = f"# Verificación documental\n\n**{estado}**\n\n- Antes: `{args.before}`\n- Después: `{args.after}`\n\n## Error\n- ❌ {bloqueos[0]}"
            Path(args.report).parent.mkdir(parents=True, exist_ok=True)
            Path(args.report).write_text(reporte_error, encoding='utf-8')
        print(f"❌ {estado}: {bloqueos[0]}")
        sys.exit(1)

    m_antes = contar_metricas(c_antes)
    m_despues = contar_metricas(c_despues)
    h_antes = extraer_encabezados(c_antes)
    h_despues = extraer_encabezados(c_despues)

    estado, bloqueos, warnings = analizar_seguridad(m_antes, m_despues, h_antes, h_despues)
    reporte = generar_reporte_markdown(estado, args.before, args.after, m_antes, m_despues, h_antes, h_despues, bloqueos, warnings)

    if args.report:
        Path(args.report).parent.mkdir(parents=True, exist_ok=True)
        Path(args.report).write_text(reporte, encoding='utf-8')
        print(f"✅ Reporte generado en: {args.report}")
    else:
        print(reporte)

    print(f"RESULTADO: {estado}")
    sys.exit(1 if estado == "VERIFY_BLOCKED" else 0)

if __name__ == "__main__":
    main()
