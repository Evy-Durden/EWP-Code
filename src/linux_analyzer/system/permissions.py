import os
import stat
from typing import Dict


def get_file_permissions(path: str) -> Dict[str, bool]:
  """
  Returns basic permission flags for a file.
  """
  st = os.stat(path)

  return {
    "world_writable": bool(st.st_mode & stat.S_IWOTH),
    "group_writable": bool(st.st_mode & stat.S_IWGRP),
    "owner_uid": st.st_uid,
    "mode_octal": oct(st.st_mode & 0o777),
  }

