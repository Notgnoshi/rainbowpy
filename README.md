# rainbowpy
> Controls an RGB LED strip via serial.

So far, with an Arduino (with 5V logic) and the RGB LED strip (USC1903 chipset) found [here](https://moderndevice.com/product/serial-rgb-led-strips-ucs1903/). Note that most any addressable RGB LED strip will work -- provided it is supported by the [FastLED](https://github.com/FastLED/FastLED) library. Also depends on [`pyserial`](https://github.com/pyserial/pyserial).

Current usage (requires the [controller](controller) sketch to be running on an Arduino):

```
~ $ ./rainbowpy.py --help
usage: rainbowpy.py [-h] [--version] device

An RGB LED strip interpreter.

positional arguments:
  device         Serial Device. Defaults to /dev/ttyUSB0

optional arguments:
  -h, --help     show this help message and exit
  --version, -v  show program's version number and exit
```

Note the user that runs the script as should be added to the `dialout` and `tty` groups in order to access the serial port. I've also had problems with Arduino sketches restarting whenever a new serial connection is made. There are ways to prevent this functionality, but they require physical modification to your Arduino. To bypass without modifying your Arduino, you can run the [sketch](controller) sketch with the Serial Monitor open. Or, you could continually have the `rainbowpy.py` script always running. This makes automation via cron jobs difficult :(

## REPL Syntax:

* `color <color>` Sets the color of the LED strip. To set the strip to red, use one of the following: `color red`, `color 255 0 0`, or `color #ff0000`. Note that Rainbowpy understands HTML5 named colors, except for RebeccaPurple.
* `dominant` Sets the primary color of the LED strip to the dominant screen color. Not yet implemented.
* `brightness <brightness>` Sets the LED strip brightness. `0..255`.
* `set correction [TypicalSMD5050 | TypicalLEDStrip | Typical8mmPixel | TypicalPixelString | UncorrectedColor]` Sets the color correction of the LED strip.
* `set temperature [Candle | Tungsten40W | Tungsten100W | Halogen | CarbonArc | HighNoonSun | DirectSunlight | OvercastSky | ClearBlueSky | WarmFluorescent | StandardFluorescent | CoolWhiteFluorescent | FullSpectrumFluorescent | GrowLightFluorescent | BlackLightFluorescent | MercuryVapor | SodiumVapor | MetalHalide | HighPressureSodium | UncorrectedTemperature]` Sets the LED color temperature.

Note the REPL supports basic tab completion of commands, but will attempt to do so unintelligently.

## TODO:
* Add alarm
    - `alarm add 8:00 am` and `alarm remove 8:00 am`? The syntax will be difficult to get right.
    - Flash the light for several minutes.
    - Enable canceling the flashing?
    - Might require threads or other async methods. How to do this without blocking execution of new commands?
* Only autocomplete valid commands. E.g. if using the `color` command, only autocomplete valid colors.
* Clean up and modularize the parser. I'm ashamed of this current garbage.
* Improve the Arduino controller...
    - Perhaps the packets could be text that the parser verifies and then passes on? This would simplify the parser, but I'm not sure I want to work with text on the Arduino.
    - Fully decide where the main set of functionality will be implemented.
        * Should this go as far as indexing individual LEDs from the Python script?
* Add better commandline options?
* Separate arduino control and commandline parsing to enable things like nonblocking flashing.
