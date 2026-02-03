from abc import ABC, abstractmethod
from typing import Iterable

from core.context import ExecutionContext
from core.models import Finding


class Check(ABC):
    """
    A single executable security check.
    """

    @property
    @abstractmethod
    def id(self) -> str:
        """Stable identifier (used for filtering, reporting, and traceability)."""
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        """Human-readable description of what the check does."""
        pass

    @abstractmethod
    def run(self, context: ExecutionContext) -> Iterable[Finding]:
        """
        Execute the check and return any findings.
        Must never raise for expected conditions.
        """
        pass

