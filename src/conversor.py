from re import compile
from validator import RE_RGB

def hex_to_rgb(value):
    """
    Converts an hexadecimal {value} to RGB.

    {value} must be a \'#\' character followed by three hexadecimal values in a range from 00 to ff.
    """
    return '{0},{1},{2}'.format(
        to_int(value[1:3]),
        to_int(value[3:5]),
        to_int(value[5:7])
    )

def to_int(value):
    return int('0x' + value, 0)

def rgb_to_hex(value):
    """
    Converts a RGB {value} to hexadecimal string.

    {value} must be three decimal values between 0 to 255 separated by a \',\' character.
    """
    extractor = compile(RE_RGB)
    extractor = extractor.match(value)
    return '#{0}{1}{2}'.format(
        to_hex(extractor.group(1)),
        to_hex(extractor.group(2)),
        to_hex(extractor.group(3))
    )

def to_hex(value):
    result = hex(int(value, 10))[2:]
    if len(result) == 1:
        result = '0' + result
    return result
