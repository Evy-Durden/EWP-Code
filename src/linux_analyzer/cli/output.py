import typer

# Base private helper

def _print(
    message: str,
    *, # enforces keyword arguments
    fg: str | None = None,
    bold: bool = False,
    err: bool = False,
    nl: bool = True,
):	
		# secho includes Rich to provide enhanced console output
    typer.secho(
        message,
        fg=fg,
        bold=bold,
        err=err,
        nl=nl,
    )


# Message types

def header(text: str):
    _print(f"\n{text}", fg="cyan", bold=True)
    _print("-" * len(text), fg="cyan")


def success(text: str):
    _print(f"✔ {text}", fg="green", bold=True)


def warning(text: str):
    _print(f"⚠ {text}", fg="yellow", bold=True)


def error(text: str):
    _print(f"✖ {text}", fg="red", bold=True, err=True)


def info(text: str):
    _print(text, fg="white")

