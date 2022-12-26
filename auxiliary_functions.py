def get_path(from_path):
    ret = ""
    if type(from_path) is str:
        return from_path + "/"
    for elem in from_path:
        ret += elem + "/"
    return ret[:-1]


def lower_first(string: str):
    return string[0].lower() + string[1:]


def dictify(string):
    after = False
    key = ""
    value = ""
    for character in string:
        if after:
            value += character
        elif character == ":":
            after = True
        else:
            key += character
    return key, value