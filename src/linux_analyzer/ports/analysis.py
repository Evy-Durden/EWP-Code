from abc import ABC, abstractmethod
from linux_analyzer.core.context import ExecutionContext
from linux_analyzer.core.models import Finding

class AnalysisStrategy(ABC):

    @abstractmethod
    def run(self, ctx: ExecutionContext) -> list[Finding]:
			...

