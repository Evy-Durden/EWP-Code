from typing import Dict, List, Optional
import pwd
import spwd


def get_local_users() -> List[Dict[str, Optional[str]]]:
  """
  Returns basic local user account information.
  """
  users = []

  for user in pwd.getpwall():
    entry = {
      "username": user.pw_name,
      "uid": user.pw_uid,
      "gid": user.pw_gid,
      "home": user.pw_dir,
      "shell": user.pw_shell,
      "password_set": None,   # best-effort
    }

    try:
      shadow = spwd.getspnam(user.pw_name)
      entry["password_set"] = shadow.sp_pwdp not in ("", "!", "*")
    except PermissionError:
      # Cannot read shadow; leave as unknown
      pass
    except KeyError:
      pass

    users.append(entry)

  return users

