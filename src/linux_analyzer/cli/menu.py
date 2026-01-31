from .prompts import prompt_choice
from .output import *


def show_menu():
		header("Welcome to the Linux Analyzer Tool")
	
		# User input
		flags = prompt_choice()
	
		if flags["mode"] == "static":
				info("You have chosen the static mode.")
		elif flags["mode"] == "behavioral":
				info("You have chosen the behavioral mode.")
		elif flags["mode"] == "full":
				info("You have chosen the full mode.")
