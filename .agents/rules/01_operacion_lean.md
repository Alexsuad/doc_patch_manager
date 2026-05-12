# Regla — Operación LEAN + 5S
Aplicar esta regla en todo el repositorio.
## Principio
No guardar basura.
## Obligatorio
- Eliminar archivos temporales que no tengan propósito.
- No mover basura a examples/ solo para conservarla.
- Mantener fixtures mínimos y útiles.
- No conservar outputs generados dentro del repo limpio.
- No crear backups manuales si el usuario ya usa utozip.
- No crear scripts nuevos si el problema se resuelve con uno existente.
- No hacer refactors grandes sin necesidad.
## Antes de eliminar
Si el archivo puede ser importante, primero buscar referencias:
`ash
grep -r " nombre_archivo\
