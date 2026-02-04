import platform

def get_kernel_version() -> str:
  return platform.release()

