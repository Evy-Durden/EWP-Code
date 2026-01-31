from typing import TypedDict

# using a typed dictionary to manage the flags
class PromptResult(TypedDict):
    mode: str
    cve: bool
    report: bool

# dictionary for base flags
BASE_FLAGS = {
		"-s": "static",
    "-b": "behavioral",
    "-f": "full",
}

# set for optional flags
OPTIONAL_FLAGS = {"-cve", "-r"}


def prompt_choice() -> PromptResult:
    while True:
        raw = input(
            "Select mode (-s | -b | -f) with optional flags [-cve] [-r]: "
        ).strip()
				
				# splitting the input into a list of flags
        tokens = raw.split()
				
				# check if there is any input at all 
        if not tokens:
            print("No input provided.")
            continue
				
				# using list comprehensions sort the flags into the right categories
        base_flags = [t for t in tokens if t in BASE_FLAGS]
        optional_flags = [t for t in tokens if t in OPTIONAL_FLAGS]
        unknown_flags = [
            t for t in tokens
            if t not in BASE_FLAGS and t not in OPTIONAL_FLAGS
        ]

        # --- Validation ---
        # checking for unkown flags
        if unknown_flags:
            print(f"Unknown flags: {', '.join(unknown_flags)}")
            continue
				
				# ensuring that exactly one base flag has been selected
        if len(base_flags) != 1:
            print("You must select exactly one of -s, -b, or -f.")
            continue
				
				# enforcing the order of base flags before optional flags
        base_index = tokens.index(base_flags[0])
        for opt in optional_flags:
            if tokens.index(opt) < base_index:
                print(f"{opt} must follow the base mode flag.")
                break
        else:
            # Returning the user input to menu
            return {
                "mode": BASE_FLAGS[base_flags[0]],
                "cve": "-cve" in optional_flags,
                "report": "-r" in optional_flags,
            }

