import shutil
from pathlib import Path
import os


from utils.path import get_safe_path


def copy(src: Path | str, dst: Path | str):
    src = get_safe_path(src, permissions=os.R_OK)
    dst = get_safe_path(dst, permissions=os.X_OK + os.W_OK, is_file=False)

    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy(src, dst)
