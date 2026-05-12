# File: src/validate_markdown_structure.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Validador determinista de estructura y limpieza Markdown.
# Versión: v1.3.1-rev3
# Rol: Gate de calidad reforzado para el Documento Maestro.
# ──────────────────────────────────────────────────────────────────────

import argparse
import sys
import re
from pathlib import Path
from datetime import datetime

class MarkdownValidator:
    def __init__(self, document_path):
        self.path = Path(document_path)
        self.blocks = []
        self.warnings = []
        self.metrics = {
            "lineas": 0,
            "h1_count": 0,
            "total_headers": 0,
            "secciones_sin_md": 0
        }
        self.status = "MARKDOWN_OK"
        self.titulo_maestro = "DOCUMENTO MAESTRO DE CRITERIOS DE ARQUITECTURA HÍBRIDA AGÉNTICA"

    def validate(self):
        if not self.path.exists():
            self.blocks.append(f"ARCHIVO_INEXISTENTE: No se encuentra {self.path}")
            self.status = "MARKDOWN_BLOCKED"
            return

        try:
            content = self.path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as e:
            self.blocks.append(f"ERROR_LECTURA: {str(e)}")
            self.status = "MARKDOWN_BLOCKED"
            return

        if not content.strip():
            self.blocks.append("ARCHIVO_VACIO: El documento no tiene contenido.")
            self.status = "MARKDOWN_BLOCKED"
            return

        # R1: Título principal duplicado (incluso texto plano)
        titulos_encontrados = re.findall(rf"(?:#\s+)?{re.escape(self.titulo_maestro)}", content, re.IGNORECASE)
        if len(titulos_encontrados) > 1:
            self.blocks.append(f"TITULO_DUPLICADO: El título principal aparece {len(titulos_encontrados)} veces (incluyendo texto plano).")

        lines = content.splitlines()
        self.metrics["lineas"] = len(lines)

        current_fence_char = None
        current_fence_len = 0
        in_code_block = False
        in_section_22 = False

        for i, line in enumerate(lines):
            line_strip = line.strip()

            # R4: Bloques de código con fences variables (3+)
            fence_match = re.match(r'^(?P<fence>`{3,}|~{3,})', line_strip)
            if fence_match:
                fence_str = fence_match.group('fence')
                if not in_code_block:
                    in_code_block = True
                    current_fence_char = fence_str[0]
                    current_fence_len = len(fence_str)
                else:
                    if fence_str[0] == current_fence_char and len(fence_str) >= current_fence_len:
                        in_code_block = False
                        current_fence_char = None
                        current_fence_len = 0

            if not in_code_block:
                # Detectar cambio de sección ANTES de evaluar H1
                if re.match(r'^\d+(\.\d+)*\.?\s+[A-Z]', line_strip):
                    if "22. " in line_strip or "22.0" in line_strip:
                        in_section_22 = True
                    elif in_section_22 and not line_strip.startswith("22."):
                        # Si es un número principal diferente a 22, salimos
                        if re.match(r'^\d+\.\s', line_strip):
                            in_section_22 = False

                # Regla de encabezados
                if line_strip.startswith("# "):
                    # R12: H1 en sección 22 (Advertencia, no cuenta para bloqueo)
                    if in_section_22 and not re.match(r'^#\s+22[\.\s]', line_strip):
                        self.warnings.append(f"L{i+1}: H1_INTERNO_SECCION_22: No recomendado fuera de bloques")
                    else:
                        self.metrics["h1_count"] += 1
                    self.metrics["total_headers"] += 1
                elif line_strip.startswith("##") or line_strip.startswith("###"):
                    self.metrics["total_headers"] += 1

                # Restos editoriales
                if "Orden de trabajo recomendado" in line_strip:
                    self.blocks.append(f"L{i+1}: RESTO_EDITORIAL: 'Orden de trabajo recomendado'")
                if "Mi recomendación inmediata" in line_strip:
                    self.blocks.append(f"L{i+1}: RESTO_EDITORIAL: 'Mi recomendación inmediata'")
                if "Nota de prueba controlada" in line_strip:
                    self.blocks.append(f"L{i+1}: RESTO_EDITORIAL: 'Nota de prueba controlada'")

                # R3: Regla aplicable rota
                if "Regla aplicable" in line_strip:
                    next_idx = i + 1
                    while next_idx < len(lines) and not lines[next_idx].strip():
                        next_idx += 1
                    if next_idx < len(lines):
                        next_line = lines[next_idx].strip()
                        if re.match(r'^(#+\s+)?\d+\.\d+', next_line):
                            self.blocks.append(f"L{i+1}: REGLA_APLICABLE_ROTA: Seguida directamente por sección {next_line}")

                # R2: Secciones numeradas sin Markdown
                if re.match(r'^\d+(\.\d+)*\.?\s+[A-Z]', line_strip) and not line_strip.startswith("#"):
                    self.metrics["secciones_sin_md"] += 1
                    self.warnings.append(f"L{i+1}: SECCION_SIN_MD: '{line_strip}'")

                # Erratas
                if "and evidencia" in line_strip:
                    self.warnings.append(f"L{i+1}: ERRATA: 'and evidencia'")
                if "hallagzos" in line_strip:
                    self.warnings.append(f"L{i+1}: ERRATA: 'hallagzos'")
                if "aprobación humana explícitamente" in line_strip:
                    self.warnings.append(f"L{i+1}: ERRATA: 'aprobación humana explícitamente'")

        if in_code_block:
            self.blocks.append("BLOQUE_CODIGO_ABIERTO: El documento termina con un bloque sin cerrar.")

        if self.metrics["h1_count"] > 1:
            self.blocks.append(f"H1_EXCESIVO: Detectados {self.metrics['h1_count']} encabezados H1.")

        if self.blocks:
            self.status = "MARKDOWN_BLOCKED"
        elif self.warnings:
            self.status = "MARKDOWN_WARNING"
        else:
            self.status = "MARKDOWN_OK"

    def generate_report(self, report_path):
        report_file = Path(report_path)
        report_file.parent.mkdir(parents=True, exist_ok=True)
        lines = [
            "# Validación de estructura Markdown", "",
            f"## Estado final: {self.status}", "",
            f"## Documento analizado: `{self.path.name}`", "",
            "## Bloqueos",
        ]
        if not self.blocks:
            lines.append("- Ninguno")
        else:
            for b in self.blocks:
                lines.append(f"- ❌ {b}")
        lines.append("")
        lines.append("## Advertencias")
        if not self.warnings:
            lines.append("- Ninguno")
        else:
            for w in self.warnings:
                lines.append(f"- ⚠️ {w}")
        lines.append("")
        lines.append("## Métricas")
        lines.append(f"- Cantidad de líneas: {self.metrics['lineas']}")
        lines.append(f"- Cantidad de encabezados H1: {self.metrics['h1_count']}")
        lines.append(f"- Cantidad de encabezados totales: {self.metrics['total_headers']}")
        lines.append(f"- Cantidad de posibles secciones numeradas sin Markdown: {self.metrics['secciones_sin_md']}")
        lines.append("")
        lines.append(f"## Fecha de ejecución: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_file.write_text("\n".join(lines), encoding="utf-8")

def main():
    parser = argparse.ArgumentParser(description="Validador de estructura Markdown")
    parser.add_argument("--document", required=True, help="Ruta al documento Markdown")
    parser.add_argument("--report", required=True, help="Ruta para el reporte de salida")
    args = parser.parse_args()
    validator = MarkdownValidator(args.document)
    validator.validate()
    validator.generate_report(args.report)
    print(f"RESULTADO: {validator.status}")
    if validator.status == "MARKDOWN_BLOCKED":
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
