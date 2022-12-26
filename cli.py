import file_reader as reader
import options
from auxiliary_functions import cls


def cli():
    cls()
    current_moves = input(
        f"""
Welcome to chess opening explorer!
Enter moves played in desired game to start searching {options.program_name}: """
)
    while True:
        cls()
        best_move = reader.get_data(current_moves)
        print(f"\nThe moves so far are |{current_moves}|" if current_moves != "" else "\n", end="")
        new_move = input(f"""
Your best move in this position is {best_move}
Enter next move played after the suggested one or click RETURN/ENTER to end program: """
)
        if new_move == "":
            break
        current_moves += " " if current_moves != "" else ""
        current_moves += best_move + " " + new_move

    cls()
    repeat = input(
        f"""
Thank you for using {options.program_name}
Do you want to repeat the program (Y/N): """
)
    while repeat not in ("Y", "N", "y", "n"):
        cls()
        repeat = input(
            f"""
Please enter "Y" if you wish to repeat the program or "N" if you want to end it: """
)
    if repeat in ("Y", "y"):
        cli()
