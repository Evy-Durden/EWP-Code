from typing import List
from linux_analyzer.core.context import ExecutionContext
from linux_analyzer.core.models import Finding
from linux_analyzer.core.ports.analysis_strategy import AnalysisStrategy

class AnalysisPipeline:
  def __init__(self, strategies: List[AnalysisStrategy]):
    self._strategies = strategies

  def run(self, context: ExecutionContext) -> List[Finding]:
    findings: List[Finding] = []

    for strategy in self._strategies:
		  findings.extend(strategy.run(context))

    return findings


