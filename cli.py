import file_reader as reader
import constants
from auxiliary_functions import cls


def cli():
    cls()
    current_moves = input(
        f"""
Welcome to chess opening explorer!
Enter moves played in desired game to start searching {constants.PROGRAM_NAME}: """
    ).strip()
    while True:
        cls()
        best_move = reader.get_data(current_moves)
        if best_move == 1:
            list_old = current_moves.split(" ")
            list_old.pop()
            current_moves = " ".join(list_old)
            if current_moves != "":
                current_moves += " "
            current_moves += input(f"""No such move exists in {constants.PROGRAM_NAME}!
\n{f'The moves so far are |{current_moves}|' if current_moves != '' else ''}
Enter next move played after the suggested one or click RETURN/ENTER to end program: """
                                   ).strip()
        else:
            print(f"\nThe moves so far are |{current_moves}|" if current_moves != "" else "\n", end="")
            new_move = input(f"""
Your best move in this position is {best_move}
Enter next move played after the suggested one or click RETURN/ENTER to end program: """
                             ).strip()
            if new_move == "":
                break
            current_moves += " " if current_moves != "" else ""
            current_moves += best_move + " " + new_move

    cls()
    repeat = input(
        f"""
Thank you for using {constants.PROGRAM_NAME}
Do you want to repeat the program (Y/N): """
    ).strip()
    while repeat not in ("Y", "N", "y", "n"):
        cls()
        repeat = input(
            f"""
Please enter "Y" if you wish to repeat the program or "N" if you want to end it: """
        ).strip()
    if repeat in ("Y", "y"):
        cli()
