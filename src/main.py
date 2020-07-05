
from sys import argv

from conversor import hex_to_rgb, rgb_to_hex
from validator import is_hex, is_rgb

def show_help():
    print('usage: {0} \'(RGB|hex)\''.format(argv[0]))
    print('\nexamples:')
    print('  {0} #000000'.format(argv[0]))
    print('  {0} 255,255,255'.format(argv[0]))


if __name__ == '__main__':
    if len(argv) < 2 or len(argv) > 2:
        show_help()
        exit(1)

    value = argv[1]
    if is_hex(value):
        print(
            hex_to_rgb(value)
        )
    elif is_rgb(value):
        print(
            rgb_to_hex(value)
        )
    else:
        print('error: invalid value')
