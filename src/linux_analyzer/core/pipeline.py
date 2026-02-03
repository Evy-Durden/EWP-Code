# core/pipeline/static_pipeline.py
from typing import List
from core.models import Finding
from core.context import ExecutionContext
from core.ports.analysis import AnalysisStrategy

class AnalysisPipeline:
  def __init__(self, strategies: list[AnalysisStrategy]):
  	self._strategies = strategies

  def run(self, context: ExecutionContext) -> list[Finding]:
    findings: list[Finding] = []

    for strategy in self._strategies:
      findings.extend(strategy.run(context))

    return findings


