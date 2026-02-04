from linux_analyzer.core.context import ExecutionContext
from linux_analyzer.core.models import Finding
from linux_analyzer.checks.base import BaseCheck
from linux_analyzer.system.os_info import kernel_version


class KernelVersionCheck(BaseCheck):

  def run(self, context: ExecutionContext) -> list[Finding]:
    kernel = kernel_version()

    # Detection logic is allowed
    if kernel.startswith("2."):
      return [
        Finding(
          id="KERNEL-001",
          title="Legacy Linux kernel detected",
          description="The system is running a Linux 2.x kernel.",
          category="kernel",
          source="static.kernel_version",
          location=None,
          evidence={
              "kernel_version": kernel,
          },
        )
      ]

    return []


