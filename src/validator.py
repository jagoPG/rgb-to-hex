from re import compile

RE_HEXADECIMAL = r'^#[a-fA-F0-9]{6}$'
RE_RGB = r'^(\d{1,3}),(\d{1,3}),(\d{1,3})$'

def is_hex(value):
    """
    Check if the provided {value} is an hexadecimal value.
    """
    validator = compile(RE_HEXADECIMAL)
    return validator.match(value) is not None


def is_rgb(value):
    """
    Check if the provided {value} is a RGB value.
    """
    validator = compile(RE_RGB)
    result = validator.match(value)
    is_valid_format = result is not None
    if not is_valid_format:
        return False
    for i in range(1, 4):
        if not is_rgb_value(int(result.group(i))):
            return False
    return True


def is_rgb_value(value):
    return value >= 0 and value <= 255
