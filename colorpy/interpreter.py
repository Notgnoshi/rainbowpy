import readline
import struct
import serial
from webcolors import name_to_rgb, hex_to_rgb
from completions import completer

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")


class Command(object):
    def __init__(self, red, green, blue, solid=True, led=None):
        self.solid = solid
        # Struct doesn't know what to do with `None`
        self.led = 0 if led is None else led
        self.red = red
        self.green = green
        self.blue = blue

    def Pack(self):
        s = struct.Struct('5B')
        return s.pack(self.solid, self.led, self.red, self.green, self.blue)


def to_rgb(args):
    rgb = (0, 0, 0)
    if len(args) == 3:
        try:
            rgb = tuple(int(i) for i in args)
        except ValueError:
            print('not a valid RGB value')
    elif len(args) == 1:
        color = args[0]
        if color.startswith('#'):
            try:
                rgb = hex_to_rgb(color)
            except ValueError:
                print('not a valid hex color code {}'.format(color))
        else:
            try:
                rgb = name_to_rgb(color)
            except ValueError:
                print('not a valid named color {}'.format(color))
    else:
        print('unrecognized color {}'.format(args))
    return rgb


class Interpreter(object):
    def __init__(self, device):
        self.serial_device = serial.Serial(device, 115200)
        self.current_color = None

    def interpret(self):
        while True:
            try:
                command = input('colorpy> ')
                self.parse_and_run(command)
            except (KeyboardInterrupt, EOFError):
                print('')
                self.serial_device.write(Command(0, 0, 0).Pack())
                self.serial_device.close()
                break

    def parse_and_run(self, command):
        tokens = [token.lower() for token in command.strip().split()]
        root_command = tokens[0]
        args = tokens[1:]

        if root_command == 'set':
            self.parse_set(args)
        elif root_command == 'transition':
            print('\ttransition not yet supported.')
        elif root_command == 'brightness':
            print('\tbrightness not yet supported.')
        else:
            print('\tunrecognized command.')

    def parse_set(self, args):
        if args[0] in ['follow', 'off', 'dominant', 'demo' 'led']:
            print('`set` subcommand `{}` not yet supported'.format(args[0]))
        else:
            self.current_color = to_rgb(args)
            self.set_color()

    def set_color(self):
        c = Command(*self.current_color, solid=True, led=0)
        self.serial_device.write(c.Pack())
