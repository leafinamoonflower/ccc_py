# on windows use cmd.exe instead of default shell:
set windows-shell := ["cmd.exe", "/c"]

alias solve := solve_singular
alias prepare := prepare_folders
alias prep := prepare_folders

prepare_folders LEVEL:
	python3 src/prepare_folders.py {{LEVEL}}

solve_example LEVEL:
	just solve_singular {{LEVEL}} 0

solve_singular LEVEL FILE:
	python3 src/solve_singular.py {{LEVEL}} {{FILE}}

solve_all LEVEL:
	python3 src/solve_all.py {{LEVEL}}