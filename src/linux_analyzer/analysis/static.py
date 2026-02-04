from linux_analyzer.core.context import ExecutionContext
from linux_analyzer.core.models import Finding
from linux_analyzer.core.ports.analysis_strategy import AnalysisStrategy

# from linux_analyzer.analysis.checks.filesystem.permissions import PermissionsCheck
# from linux_analyzer.analysis.checks.users.accounts import UserAccountsCheck
from linux_analyzer.analysis.checks.system.kernel_version import KernelVersionCheck


class StaticAnalysisStrategy(AnalysisStrategy):
  def __init__(self) -> None:
    self.checks = [
      KernelVersionCheck(),
      # PermissionsCheck(),
      # UserAccountsCheck(),
    ]

  def run(self, context: ExecutionContext) -> list[Finding]:
    findings: list[Finding] = []

    for check in self.checks:
      findings.extend(check.run(context))

    return findings

