#!/usr/bin/env python3
import serial
import struct
import argparse


class Color(object):
    def __init__(self, red, green, blue, solid=True, led=None):
        self.solid = solid
        # Struct doesn't know what to do with `None`
        self.led = 0 if led is None else led
        self.red = red
        self.green = green
        self.blue = blue

    def Pack(self):
        s = struct.Struct('BBBBB')
        return s.pack(self.solid, self.led, self.red, self.green, self.blue)


def main(device, solid, led, red, green, blue):
    ser = serial.Serial(device, 115200)
    color = Color(red, green, blue, solid, led)
    ser.write(color.Pack())
    ser.close()


if __name__ == '__main__':
    VERSION = 'Colorpy version 0.0.1 by Austin Gill'
    DESCRIPTION = 'Controls an RGB LED strip via serial connection with an Arduino'
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--version', '-v', action='version', version=VERSION)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--solid', '-s', action='store_true', default=True,
                       help='Set strip to solid color. Default.')
    group.add_argument('--led', '-l', type=int,
                       help='The LED you wish to set')
    parser.add_argument('--device', '-d', default='/dev/ttyACM0', type=str,
                        help='Serial Device. Defaults to /dev/ttyACM0')
    parser.add_argument('R', type=int, help='RED color value to send 0..255')
    parser.add_argument('G', type=int, help='GREEN color value to send 0..255')
    parser.add_argument('B', type=int, help='BLUE color value to send 0..255')
    args = parser.parse_args()

    # args.solid defaults to True, so if we set the number of LEDs, turn off solid
    if args.led is not None:
        args.solid = False

    main(args.device, args.solid, args.led, args.R, args.G, args.B)
