from pathlib import Path
def cargar_contenido(p): return p.read_text(encoding='utf-8')
def guardar_contenido(p, c): 
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(c, encoding='utf-8')
