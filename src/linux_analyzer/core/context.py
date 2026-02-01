from dataclasses import dataclass
from typing import Optional, Literal

@dataclass
class ExecutionContext:
	"""
	This class harbours all the information to give the execution context.
	It provides information of the system and what is allowed to be done.
	Responisibilities: OS and kernel info, privilege level, runtime flags, environment constraints
	"""
	# mirror user input
	mode: Literal["static", "behavioral", "full"]
	enable_cve_lookup: bool
	generate_report: bool

	# further information
	"""
	discovered: bool = False
	os: Optional[str] = None
	kernel_version: Optional[str] = None
	is_root: Optional[bool] = None
	ebpf_available: Optional[bool] = None
	"""
