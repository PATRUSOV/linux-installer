import shutil
from pathlib import Path
import os
from utils.path import normalize_path
from utils.path import validate_path


def copy(src: Path | str, dst: Path | str):
    src = normalize_path(src)
    dst = normalize_path(dst)
    validate_path(src, permissions=os.R_OK)
    validate_path(dst, permissions=os.X_OK + os.W_OK, is_file=False)

    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy(src, dst)
