#!/usr/bin/python3
import argparse
from interpreter import Interpreter


def main(device):
    intereter = Interpreter(device)
    intereter.interpret()


if __name__ == '__main__':
    VERSION = 'Colorpy version 0.0.2 by Austin Gill'
    DESCRIPTION = 'An RGB LED strip interpreter.'
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('--version', '-v', action='version', version=VERSION)
    parser.add_argument('device', default='/dev/ttyACM0', type=str,
                        help='Serial Device. Defaults to /dev/ttyACM0')

    args = parser.parse_args()
    main(args.device)
