# core/models.py
from dataclasses import dataclass, field
from typing import Any, Dict, Optional, List, Literal


@dataclass(frozen=True)
class Finding:
	"""
	This class simply records what and where something was found by the analyzers.
	"""
  id: str
  title: str
  description: str

  category: str            # e.g. "kernel", "syscall", "config"
  source: str              # analyzer name, e.g. "lsm_static"

  location: Optional[str]  # file path, syscall name, module, etc.
  evidence: Dict[str, Any] = field(default_factory=dict)



Severity = Literal["info", "low", "medium", "high", "critical"]


@dataclass(frozen=True)
class EvaluationResult:
	"""
	It displays the intepretation of a finding. It never modifies the finding.
	"""
  finding_id: str

  severity: Severity
  confidence: float          # 0.0 – 1.0

  summary: str               # short human-readable verdict
  rationale: str             # why this severity was chosen

  cves: List[str] = field(default_factory=list)
  references: List[str] = field(default_factory=list)





