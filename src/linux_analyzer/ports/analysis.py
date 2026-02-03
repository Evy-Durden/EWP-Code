from abc import ABC, abstractmethod
from linux_analyzer.core.context import ExecutionContext
from linux_analyzer.core.models import Finding
from typing import List

class AnalysisStrategy(ABC):

    @abstractmethod
    def run(self, context: ExecutionContext) -> List[Finding]:
        ...

