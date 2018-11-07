import cx_Freeze

executables = [cx_Freeze.Executable("breakout.py")]

cx_Freeze.setup(
    name = "Breakout",
    options = {"build_exe":{"packages":["pygame"], "include_files":["fonts/AtariClassic-Regular.ttf"]}},
    description = "Breakout Game",
    executables = executables
)