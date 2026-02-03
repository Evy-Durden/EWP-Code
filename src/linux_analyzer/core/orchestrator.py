from linux_analyzer.core.context import ExecutionContext
from linux_analyzer.core.pipeline import AnalysisPipeline

def run(context: ExecutionContext) -> None:
    """
    Trusted entry point from the CLI into the core meaning it is the trust boundary.
    Everything before the orchestrator is user-controlled and everything after is internal.
    It acts as the gatekeeper, decides whether pipeline runs.
    It owns the entire lifecyle from start to finish.
    """

    #if context.generate_report:


