from abc import ABC, abstractmethod
from linux_analyzer.core.context import ExecutionContext
from linux_analyzer.core.models import Finding


class BaseCheck(ABC):

  @abstractmethod
  def run(self, context: ExecutionContext) -> list[Finding]:
    ...

