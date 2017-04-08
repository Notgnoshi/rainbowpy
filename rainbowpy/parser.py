import struct
import webcolors


class Parser(object):
    # note the parser lowercases everything when it tokenizes, so make sure these are all lowercase
    root_keywords = ['set', 'primary', 'secondary', 'dominant', 'led', 'brightness', 'clear']

    temperatures = [
        'candle',
        'tungsten40w',
        'tungsten100w',
        'halogen',
        'carbonarc',
        'highnoonsun',
        'directsunlight',
        'overcastsky',
        'clearbluesky',
        'warmfluorescent',
        'standardfluorescent',
        'coolwhitefluorescent',
        'fullspectrumfluorescent',
        'growlightfluorescent',
        'blacklightfluorescent',
        'mercuryvapor',
        'sodiumvapor',
        'metalhalide',
        'highpressuresodium',
        'uncorrectedtemperature',
    ]

    corrections = [
        'typicalsmd5050',
        'typicalledstrip',
        'typical8mmpixel',
        'typicalpixelstring',
        'uncorrectedcolor',
    ]

    SET_PRIMARY_COLOR = 10
    SET_SECONDARY_COLOR = 20
    SET_BRIGHTNESS = 30
    SET_TRANSITION = 40
    SET_MODE = 50
    SET_COLOR_CORRECTION = 60
    SET_COLOR_TEMPERATURE = 70

    def __init__(self):
        self.struct = struct.Struct('4B')

    def parse(self, command):
        tokens = command.lower().strip().split()
        root = tokens.pop(0)

        if root not in self.root_keywords:
            print('\t`{}` is not a recognized root command'.format(root))
            return None

        if root == 'set':
            return self._set(tokens)
        elif root == 'primary':
            return self._primary(self._to_color(tokens))
        elif root == 'secondary':
            return self._secondary(self._to_color(tokens))
        elif root == 'dominant':
            return self._dominant_color()
        elif root == 'brightness':
            return self._brightness(tokens)
        else:
            return None

    def _set(self, tokens):
        root = tokens.pop(0)
        if root not in ['transition', 'mode', 'correction', 'temperature']:
            print('\t`{}` is not a recognized `set` subcommand'.format(root))
            return None

        if root == 'correction':
            return self._set_correction(tokens)
        elif root == 'temperature':
            return self._set_temperature(tokens)
        elif root == 'mode':
            print('\t`mode` not yet supported')
            return None
        elif root == 'transition':
            print('\t`transition` not yet supported')
            return None
        else:
            return None

    def _set_correction(self, tokens):
        correction = tokens[0]
        try:
            c = self.corrections.index(correction)
            return self.struct.pack(self.SET_COLOR_CORRECTION, c, 0, 0)
        except ValueError:
            print('\tcorrection `{}` not found'.format(correction))
            return None

    def _set_temperature(self, tokens):
        temp = tokens[0]
        try:
            t = self.temperatures.index(temp)
            return self.struct.pack(self.SET_COLOR_TEMPERATURE, t, 0, 0)
        except ValueError:
            print('\ttemperature `{}` not found'.format(temp))
            return None

    def _to_color(self, tokens):
        rgb = None
        if len(tokens) is 3:
            try:
                rgb = [int(i) for i in tokens]
            except ValueError:
                print('\tmalformed color `{}`'.format(tokens))
        elif tokens[0].startswith('#'):
            try:
                rgb = webcolors.hex_to_rgb(tokens[0])
            except ValueError:
                print('\tmalformed color `{}`'.format(tokens[0]))
        else:
            try:
                rgb = webcolors.name_to_rgb(tokens[0])
            except ValueError:
                print('\tmalformed color `{}`'.format(tokens[0]))
            # print('\tRGB: ', rgb)
        return rgb

    def _primary(self, rgb):
        if rgb is not None:
            return self.struct.pack(self.SET_PRIMARY_COLOR, *rgb)
        else:
            return None

    def _secondary(self, rgb):
        if rgb is not None:
            return self.struct.pack(self.SET_SECONDARY_COLOR, *rgb)
        else:
            return None

    def _dominant_color(self):
        print('\tDominant Screen color not yet implemented')
        return None

    def _brightness(self, tokens):
        if tokens[0].isdecimal():
            brightness = int(tokens[0])
            return self.struct.pack(self.SET_BRIGHTNESS, brightness, 0, 0)
        else:
            return None
