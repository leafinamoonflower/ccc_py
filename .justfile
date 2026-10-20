# on windows use cmd.exe instead of default shell:
set windows-shell := ["cmd.exe", "/c"]
set quiet

export PYTHONPATH := "./src"

alias solve := solve_singular
alias s := solve_singular
alias se := solve_example
alias sa := solve_all
alias prepare := prepare_folders
alias prep := prepare_folders
alias p := prepare_folders

prepare_folders LEVEL:
	python src/scripts/prepare_folders.py {{LEVEL}}

solve_example LEVEL:
	just solve_singular {{LEVEL}} 0

solve_singular LEVEL FILE:
	python src/scripts/solve_singular.py {{LEVEL}} {{FILE}}

solve_all LEVEL:
	python src/scripts/solve_all.py {{LEVEL}}
