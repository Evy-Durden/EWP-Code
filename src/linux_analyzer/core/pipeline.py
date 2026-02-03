# core/pipeline/static_pipeline.py
from typing import List
from linux_analyzer.core.models import Finding
from linux_analyzer.core.context import ExecutionContext
from linux_analyzer.ports.analysis import AnalysisStrategy

class AnalysisPipeline:
  def __init__(self, strategies: list[AnalysisStrategy]):
  	self._strategies = strategies

  def run(self, context: ExecutionContext) -> list[Finding]:
    findings: list[Finding] = []

    for strategy in self._strategies:
      findings.extend(strategy.run(context))

    return findings


