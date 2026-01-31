import typer
from .menu import show_menu

# creating a typer app
app = typer.Typer()

@app.command()
def main():
	"""
	The @app.command() decorator turns a function into a CLI command.
	Main simple calls into menu.py and does not implement any menu logic itself.
	The reason is separation of concern for testability, readability and maintainability.
	"""
	show_menu()
	
# ensure that code is only run when script is executed and not when it is imported
if __name__ == "__main__":
	app()

