from platform import system as system_name
from subprocess import  call as system_call

import constants


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


def cls():
    command = 'cls' if system_name().lower().startswith('win') else 'clear'
    system_call([command])


def safe_input(input_text, error_message):
    ret = None
    try:
        ret = input(input_text).strip()
        if not constants.CASE_SENSITIVE:
            ret = ret.lower()
    except KeyboardInterrupt:
        print(error_message)
    return ret
