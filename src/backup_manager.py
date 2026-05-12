import shutil
from pathlib import Path
from datetime import datetime
def crear_backup(orig, folder):
    folder.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = folder / f"{orig.stem}_{ts}{orig.suffix}"
    shutil.copy2(orig, dst)
    return dst
