---
trigger: always_on
---

# Regla transversal — Operación LEAN + 5S

Esta regla es de aplicación obligatoria en todo el repositorio para garantizar la limpieza, el orden y la eficiencia operativa.

## Principio fundamental
**"No guardar basura"**. Cada archivo, script o dato en el repositorio debe tener un propósito claro, estar vigente y estar ubicado en su lugar correspondiente.

## Obligaciones de limpieza
- **Eliminar temporales:** Borrar archivos `.tmp`, `.log`, o cualquier archivo de trabajo que ya no sea necesario.
- **No desplazar la basura:** Está prohibido mover archivos obsoletos a carpetas como `examples/` o `sandbox/` solo para evitar borrarlos. Si no sirve, se elimina.
- **Evitar redundancia:** No crear scripts nuevos si el problema puede resolverse con herramientas existentes o comandos de sistema.
- **Gestión de backups:** No crear copias de seguridad manuales dentro del repositorio (ej. `archivo_old.py`, `copia_1.json`) si el usuario ya utiliza herramientas de respaldo automático como `autozip`.
- **Outputs externos:** No conservar archivos generados (`output/`) dentro del control de versiones, a menos que sean plantillas o evidencias requeridas explícitamente.

## Antes de eliminar
Antes de borrar cualquier archivo que no sea claramente basura, se debe verificar su impacto buscando referencias activas en el proyecto:

```bash
grep -r "nombre_archivo" .
```

Si existen referencias activas, el archivo no debe eliminarse hasta que se comprenda su función y se actualicen dichas referencias.

## Criterio de limpieza (5S)
Un archivo es candidato a eliminación inmediata si cumple una o más de estas condiciones:
1. Es un archivo temporal de ejecución o depuración.
2. Es un resultado (`output`) generado automáticamente que ya ha sido verificado.
3. Es un backup manual redundante.
4. Es una prueba (`test`) duplicada que no aporta cobertura adicional.
5. Es un script de reparación puntual cuya tarea ya finalizó.
6. No tiene referencias activas ni función operativa en el sistema actual.

## Evidencia mínima de limpieza
Al realizar una tarea de limpieza o mantenimiento, se debe informar de:
- Lista de archivos eliminados.
- Motivo de la eliminación (justificación LEAN).
- Comando de verificación de referencias utilizado.
- Resultado de `uv run pytest` si la eliminación afecta a código, configuración o infraestructura de pruebas.

## Prohibiciones
- **Prohibido borrar documentos base:** Nunca eliminar archivos en `input/documentos_base/` sin aprobación humana explícita.
- **Prohibido borrar tests para "limpiar" fallos:** No se eliminan pruebas para que la suite pase; se arregla el código o se actualiza el test.
- **Prohibido el "hoarding":** No conservar archivos "por si acaso" si no hay un plan de uso documentado.
- **Prohibido ensuciar la raíz:** No dejar archivos sueltos en la raíz del repositorio que pertenezcan a carpetas específicas.
