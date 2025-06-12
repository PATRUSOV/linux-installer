import shutil
from pathlib import Path
import os
from utils.path import get_safe_path


def copy(src: Path | str, dst: Path | str, raw: bool = False):
    """Утилита для копирования, работает и с файлами, и с директориями
    args:
        src: Путь к копируемому
        dst: Куда копировать (обязатольно директоория)
        raw: Валидиривать ли аргументы
    """

    if not raw:
        src = get_safe_path(src, permissions=os.R_OK)
        dst = get_safe_path(dst, permissions=os.X_OK + os.W_OK, is_file=False)

    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy(src, dst)
