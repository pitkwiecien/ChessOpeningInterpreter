import file_reader as reader
import constants
from auxiliary_functions import cls


def cli():
    cls()
    print("Welcome to chess opening explorer!")
    current_moves = input(f"Enter moves played in desired game to start searching {constants.PROGRAM_NAME}: ").strip()
    while True:
        cls()
        best_move = reader.get_data(current_moves)
        if best_move == 1:
            list_old = current_moves.split(constants.MOVE_SEPARATOR)
            list_old.pop()
            current_moves = constants.MOVE_SEPARATOR.join(list_old)
            if current_moves != "":
                current_moves += constants.MOVE_SEPARATOR
            print(f"No such move exists in {constants.PROGRAM_NAME}!\n")
            if current_moves != '':
                sep_len = len(constants.MOVE_SEPARATOR)
                moves = constants.MOVE_HISTORY_BORDER + current_moves[:-sep_len] + constants.MOVE_HISTORY_BORDER
                print(f'The moves so far are {moves}')
            current_moves += input("Enter next move played after the suggested one or click RETURN/ENTER to end "
                                   "program: ").strip()
        else:
            if current_moves != "":
                moves = constants.MOVE_HISTORY_BORDER + current_moves + constants.MOVE_HISTORY_BORDER
                print(f"\nThe moves so far are {moves}")
            else:
                print()
            print(f"Your best move in this position is {best_move}")
            new_move = input("Enter next move played after the suggested one or click RETURN/ENTER to end program: ")\
                .strip()
            if new_move == "":
                break
            current_moves += constants.MOVE_SEPARATOR if current_moves != "" else ""
            current_moves += best_move + constants.MOVE_SEPARATOR + new_move

    cls()
    print(f"\nThank you for using {constants.PROGRAM_NAME}!")
    repeat = input("Do you want to repeat the program (Y/N): ").strip()
    while repeat not in ("Y", "N", "y", "n"):
        cls()
        repeat = input("Please enter 'Y' if you wish to repeat the program or 'N' if you want to end it: ").strip()
    if repeat in ("Y", "y"):
        print()
        cli()
