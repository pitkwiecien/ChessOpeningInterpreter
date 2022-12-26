import options, auxiliary_functions


def get_data(opening_str):
    opening_list = opening_str.split(" ")

    white = len(opening_list) % 2 == 0
    current_file = f"for{'White' if white else 'Black'}"
    filename = f"{options.openings_path}/{current_file}.txt"
    with open(filename, "r") as file:
        obj = ""
        for line in file:
            obj += format_line(line, current_file, ())
        if not white:
            obj = "{" + obj + "}"
        return retrieve_move(read_object(obj, opening_list, True if white else False))


def format_line(line, file_sender, file_history):
    ret = ""

    after_import_against = None
    to_import = ""
    whitespaces = (" ", "\n", "\t")
    for character in line:
        if character == options.comment_character:
            break

        if after_import_against is not None and character not in whitespaces:
            to_import += character

        if character == options.import_character:
            after_import_against = False
        elif character == options.import_character_against:
            after_import_against = True
        elif character not in whitespaces and after_import_against is None:
            ret += character
    if after_import_against:
        to_import = "Vs" + to_import
    if after_import_against is not None:
        ret += import_file(to_import, file_sender, file_history)
    if len(ret) == 0:
        return ""
    elif ret[-1] != "{":
        ret += "|"
    # print(ret)
    return ret


def read_object(obj, move_list, pop_first=True):
    if obj[-1] == "|":
        obj = obj[:-1]
    obj = obj.replace("|}", "}")

    mutable_move_list = list(move_list)

    after = False
    inner_object_str = ""
    parth_count = 0
    for character in obj:
        if character == "}":
            parth_count -= 1
            if parth_count == 0:
                break
        if after:
            inner_object_str += character
        if character == "{":
            after = True
            parth_count += 1
    inner_object = inner_object_str.split("|")

    inner_object_dict = dict()
    for elem in inner_object:
        key, value = auxiliary_functions.dictify(elem)
        inner_object_dict[key] = value

    if pop_first:
        mutable_move_list.pop(0)

    element_retrieved = inner_object_dict[mutable_move_list[0]]

    if len(mutable_move_list) < 2:
        return element_retrieved
    else:
        mutable_move_list.pop(0)
        return read_object(element_retrieved, tuple(mutable_move_list))


def retrieve_move(obj):
    ret = ""
    for character in obj:
        if character in ("{", "}"):
            break
        ret += character
    return ret


def import_file(filename, from_file, previous_path=()):
    # print(f"filename: {filename}, for_white: {for_white}, from_file: {from_file}, previous_path: {previous_path}")
    from_file = auxiliary_functions.lower_first(from_file)
    full_path = f"{options.openings_path}/{auxiliary_functions.get_path(previous_path)}/{from_file}/{filename}.txt"
    new_history = list(previous_path)
    new_history.append(from_file)
    with open(full_path, "r") as file:
        obj = ""
        for line in file:
            obj += format_line(line, filename, new_history)
        return obj
