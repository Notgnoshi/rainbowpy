#!/usr/bin/env python3
import argparse
import readline
from parser import Parser
import serial
from completions import Completer, OPTIONS

readline.set_completer(Completer(OPTIONS).complete)
readline.parse_and_bind("tab: complete")


def main(device):
    command_parser = Parser()
    ser = serial.Serial(device, 115200)
    while True:
        try:
            command = input('rainbowpy> ')
            struct = command_parser.parse(command)
            if struct is not None:
                ser.write(struct)
        except (KeyboardInterrupt, EOFError):
            print()
            break
    ser.write(command_parser.parse('color black'))
    ser.close()


if __name__ == '__main__':
    VERSION = 'Rainbowpy version 0.0.2 by Austin Gill'
    DESCRIPTION = 'An RGB LED strip interpreter.'
    arg_parser = argparse.ArgumentParser(description=DESCRIPTION)
    arg_parser.add_argument('--version', '-v', action='version', version=VERSION)
    arg_parser.add_argument('device', default='/dev/ttyUSB0', type=str,
                            help='Serial Device. Defaults to /dev/ttyUSB0')

    args = arg_parser.parse_args()
    main(args.device)
