import readline

COLORS = [
    'IndianRed',
    'LightCoral',
    'Salmon',
    'DarkSalmon',
    'LightSalmon',
    'Crimson',
    'Red',
    'FireBrick',
    'DarkRed',
    'Pink',
    'LightPink',
    'HotPink',
    'DeepPink',
    'MediumVioletRed',
    'PaleVioletRed',
    'Coral',
    'Tomato',
    'OrangeRed',
    'DarkOrange',
    'Orange',
    'Gold',
    'Yellow',
    'LightYellow',
    'LemonChiffon',
    'LightGoldenrodYellow',
    'PapayaWhip',
    'Moccasin',
    'PeachPuff',
    'PaleGoldenrod',
    'Khaki',
    'DarkKhaki',
    'Lavender',
    'Thistle',
    'Plum',
    'Violet',
    'Orchid',
    'Fuchsia',
    'Magenta',
    'MediumOrchid',
    'MediumPurple',
    'BlueViolet',
    'DarkViolet',
    'DarkOrchid',
    'DarkMagenta',
    'Purple',
    # 'RebeccaPurple',
    'Indigo',
    'MediumSlateBlue',
    'SlateBlue',
    'DarkSlateBlue',
    'GreenYellow',
    'Chartreuse',
    'LawnGreen',
    'Lime',
    'LimeGreen',
    'PaleGreen',
    'LightGreen',
    'MediumSpringGreen',
    'SpringGreen',
    'MediumSeaGreen',
    'SeaGreen',
    'ForestGreen',
    'Green',
    'DarkGreen',
    'YellowGreen',
    'OliveDrab',
    'Olive',
    'DarkOliveGreen',
    'MediumAquamarine',
    'DarkSeaGreen',
    'LightSeaGreen',
    'DarkCyan',
    'Teal',
    'Aqua',
    'Cyan',
    'LightCyan',
    'PaleTurquoise',
    'Aquamarine',
    'Turquoise',
    'MediumTurquoise',
    'DarkTurquoise',
    'CadetBlue',
    'SteelBlue',
    'LightSteelBlue',
    'PowderBlue',
    'LightBlue',
    'SkyBlue',
    'LightSkyBlue',
    'DeepSkyBlue',
    'DodgerBlue',
    'CornflowerBlue',
    'RoyalBlue',
    'Blue',
    'MediumBlue',
    'DarkBlue',
    'Navy',
    'MidnightBlue',
    'Cornsilk',
    'BlanchedAlmond',
    'Bisque',
    'NavajoWhite',
    'Wheat',
    'BurlyWood',
    'Tan',
    'RosyBrown',
    'SandyBrown',
    'Goldenrod',
    'DarkGoldenrod',
    'Peru',
    'Chocolate',
    'SaddleBrown',
    'Sienna',
    'Brown',
    'Maroon',
    'White',
    'Snow',
    'Honeydew',
    'MintCream',
    'Azure',
    'AliceBlue',
    'GhostWhite',
    'WhiteSmoke',
    'Seashell',
    'Beige',
    'OldLace',
    'FloralWhite',
    'Ivory',
    'AntiqueWhite',
    'Linen',
    'LavenderBlush',
    'MistyRose',
    'Gainsboro',
    'LightGray',
    'LightGrey',
    'Silver',
    'DarkGray',
    'DarkGrey',
    'Gray',
    'Grey',
    'DimGray',
    'DimGrey',
    'LightSlateGray',
    'LightSlateGrey',
    'SlateGray',
    'SlateGrey',
    'DarkSlateGray',
    'DarkSlateGrey',
    'Black'
]

CORRECTIONS = [
    'TypicalSMD5050',
    'TypicalLEDStrip',
    'Typical8mmPixel',
    'TypicalPixelString',
    'UncorrectedColor',
]

TEMPERATURES = [
    'Candle',
    'Tungsten40W',
    'Tungsten100W',
    'Halogen',
    'CarbonArc',
    'HighNoonSun',
    'DirectSunlight',
    'OvercastSky',
    'ClearBlueSky',
    'WarmFluorescent',
    'StandardFluorescent',
    'CoolWhiteFluorescent',
    'FullSpectrumFluorescent',
    'GrowLightFluorescent',
    'BlackLightFluorescent',
    'MercuryVapor',
    'SodiumVapor',
    'MetalHalide',
    'HighPressureSodium',
    'UncorrectedTemperature',
]

OPTIONS = {
    'color': COLORS,
    'correction': CORRECTIONS,
    'temperature': TEMPERATURES,
    'dominant': [],
    'alarm': ['set', 'remove'],
}


# Taken from https://pymotw.com/2/readline/
class Completer(object):
    def __init__(self, options):
        self.options = options
        self.current_candidates = []
        return

    def complete(self, text, state):
        response = None

        # This is the first time for this text, so build a match list.
        if state == 0:
            origline = readline.get_line_buffer().lower()
            begin = readline.get_begidx()
            end = readline.get_endidx()
            being_completed = origline[begin:end]
            words = origline.split()

            if not words:
                self.current_candidates = sorted(self.options.keys())
            else:
                try:
                    if begin == 0:
                        # first word
                        candidates = self.options.keys()
                    else:
                        # later word
                        first = words[0]
                        candidates = self.options[first]

                    if being_completed:
                        # match options with portion of input
                        # being completed
                        self.current_candidates = [w for w in candidates
                                                   if w.lower().startswith(being_completed)]
                    else:
                        # matching empty string so use all candidates
                        self.current_candidates = candidates

                except (KeyError, IndexError):
                    self.current_candidates = []

        try:
            response = self.current_candidates[state]
        except IndexError:
            response = None
        return response
