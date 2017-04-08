#!/usr/bin/python3
import argparse
import serial
from parser import Parser
import readline
from completions import completer

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")


def main(device):
    parser = Parser()
    ser = serial.Serial(device, 115200)
    while True:
        try:
            command = input('rainbowpy> ')
            struct = parser.parse(command)
            if struct is not None:
                ser.write(struct)
        except (KeyboardInterrupt, EOFError):
            print()
            break
    ser.write(parser.parse('primary black'))
    ser.close()


if __name__ == '__main__':
    VERSION = 'Rainbowpy version 0.0.2 by Austin Gill'
    DESCRIPTION = 'An RGB LED strip interpreter.'
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--version', '-v', action='version', version=VERSION)
    parser.add_argument('device', default='/dev/ttyUSB0', type=str,
                        help='Serial Device. Defaults to /dev/ttyUSB0')

    args = parser.parse_args()
    main(args.device)
