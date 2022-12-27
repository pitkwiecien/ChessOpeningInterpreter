import constants
import auxiliary_functions as aux


def get_data(opening_str):
    opening_list = opening_str.split(constants.MOVE_SEPARATOR)
    if opening_str == "":
        opening_list = []

    white = len(opening_list) % 2 == 0
    current_file = constants.PRIMARY_WHITE if white else constants.PRIMARY_BLACK
    filename = f"{constants.OPENINGS_PATH}/{current_file}.{constants.OPENINGS_EXTENSION}"

    if opening_str == "":
        with open(filename, "r") as file:
            line = file.readline()
            formatted_line = format_line(line, opening_list, True)
            return formatted_line[:-1]

    with open(filename, "r") as file:
        obj = ""
        for line in file:
            obj += format_line(line, current_file, ())
        if not constants.CASE_SENSITIVE:
            obj = obj.lower()
        if not white:
            obj = constants.OPENING_OBJECT_CHARACTER + obj + constants.CLOSING_OBJECT_CHARACTER
        return retrieve_move(read_object(obj, opening_list, True if white else False))


def format_line(line, file_sender, file_history):
    ret = ""

    after_import_against = None
    to_import = ""
    whitespaces = (" ", "\n", "\t")
    for character in line:
        if character == constants.COMMENT_CHARACTER:
            break

        if after_import_against is not None and character not in whitespaces:
            to_import += character

        if character == constants.IMPORT_CHARACTER:
            after_import_against = False
        elif character == constants.IMPORT_CHARACTER_AGAINST:
            after_import_against = True
        elif character not in whitespaces and after_import_against is None:
            ret += character
    if after_import_against:
        to_import = constants.OPENINGS_COUNTER_PREFIX + to_import
    if after_import_against is not None:
        ret += import_file(to_import, file_sender, file_history)
    if len(ret) == 0:
        return ""
    elif ret[-1] != constants.OPENING_OBJECT_CHARACTER:
        ret += "|"
    # print(ret)
    return ret


def read_object(obj, move_list, pop_first=True):
    if obj[-1] == "|":
        obj = obj[:-1]
    obj = obj.replace(f"|{constants.CLOSING_OBJECT_CHARACTER}", constants.CLOSING_OBJECT_CHARACTER)

    mutable_move_list = list(move_list)

    after = False
    inner_object_str = ""
    parth_count = 0
    for character in obj:
        if character == constants.CLOSING_OBJECT_CHARACTER:
            parth_count -= 1
            if parth_count == 0:
                break
        if after:
            inner_object_str += character
        if character == constants.OPENING_OBJECT_CHARACTER:
            after = True
            parth_count += 1
    inner_object = inner_object_str.split("|")

    inner_object_dict = dict()
    for elem in inner_object:
        key, value = aux.dictify(elem)
        inner_object_dict[key] = value

    if pop_first:
        mutable_move_list.pop(0)

    try:
        element_retrieved = inner_object_dict[mutable_move_list[0]]
    except KeyError:
        return KeyError

    if len(mutable_move_list) < 2:
        return element_retrieved
    else:
        mutable_move_list.pop(0)
        return read_object(element_retrieved, tuple(mutable_move_list))


def retrieve_move(obj):
    ret = ""
    if obj is KeyError:
        return 1
    for character in obj:
        if character in (constants.OPENING_OBJECT_CHARACTER, constants.CLOSING_OBJECT_CHARACTER):
            break
        ret += character
    return ret


def import_file(filename, from_file, previous_path=()):
    # print(f"filename: {filename}, from_file: {from_file}, previous_path: {previous_path}")
    from_file = aux.lower_first(from_file)
    path = f"{constants.OPENINGS_PATH}/{aux.get_path(previous_path)}"
    full_path = f"{path}/{from_file}/{filename}.{constants.OPENINGS_EXTENSION}"
    new_history = list(previous_path)
    new_history.append(from_file)
    with open(full_path, "r") as file:
        obj = ""
        for line in file:
            obj += format_line(line, filename, new_history)
        return obj
