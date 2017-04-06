import readline
import struct
import serial


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


class Interpreter(object):
    def __init__(self, device):
        self.serial_device = serial.Serial(device, 115200)
        self.current_color = None

    def interpret(self):
        while True:
            try:
                command = input('colorpy> ')
                self.parse(command)
            except (KeyboardInterrupt, EOFError):
                print('')
                self.serial_device.write(Command(0, 0, 0).Pack())
                self.serial_device.close()
                break

    def parse(self, command):
        tokens = command.strip().split()
        root_command = tokens[0].lower()
        args = tokens[1:]

        if root_command == 'set':
            self.set(args)
        elif root_command == 'led':
            self.led(args)
        elif root_command == 'transition':
            print('\ttransition not yet supported.')
        elif root_command == 'brightness':
            print('\tbrightness not yet supported.')
        else:
            print('\tunrecognized command.')

    def set(self, args):
        if len(args) is not 3:
            print('\tMust supply <R G B>')
        else:
            red, green, blue = [int(i) for i in args]
            command = Command(red, green, blue)
            self.serial_device.write(command.Pack())

    def led(self, args):
        if len(args) is not 4:
            print('\tMust supply <LED> <R G B>')
        else:
            led, red, green, blue = [int(i) for i in args]
            command = Command(red, green, blue, False, led)
            self.serial_device.write(command.Pack())
