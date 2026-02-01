import typer
from .menu import show_menu
from linux_analyzer.core.context import ExecutionContext
# from linux_analyzer.core.orchestrator import run

# creating a typer app
app = typer.Typer()

@app.command()
def main():
	"""
	The @app.command() decorator turns a function into a CLI command.
	Main simple calls into menu.py and does not implement any menu logic itself.
	The reason is separation of concern for testability, readability and maintainability.
	
	It further passes the execution context to the orchestration of the core.
	"""
	flags = show_menu()
	
	context = ExecutionContext(
		mode = flags["mode"],
		enable_cve_lookup = flags["cve"],
		generate_report = flags["report"]
	)
	
	# run(context)
	
# ensure that code is only run when script is executed and not when it is imported
if __name__ == "__main__":
	app()

