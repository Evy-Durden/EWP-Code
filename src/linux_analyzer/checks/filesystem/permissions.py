from linux_analyzer.core.context import ExecutionContext
from linux_analyzer.core.models import Finding
from linux_analyzer.checks.base import BaseCheck
from linux_analyzer.system.filesystem.permissions import get_file_permissions


SENSITIVE_PATHS = [
  "/etc/passwd",
  "/etc/shadow",
  "/etc/sudoers",
]


class PermissionsCheck(BaseCheck):

  def run(self, context: ExecutionContext) -> list[Finding]:
    findings: list[Finding] = []

    for path in SENSITIVE_PATHS:
      try:
        perms = get_file_permissions(path)
      except FileNotFoundError:
        continue
      except PermissionError:
        continue

      if perms["world_writable"]:
        findings.append(
          Finding(
            id="FS-001",
            title="World-writable sensitive file",
            description="A sensitive system file is world-writable.",
            category="filesystem",
            source="static.permissions",
            location=path,
            evidence=perms,
          )
        )

    return findings

