# rainbowpy
> Controls an RGB LED strip via serial.

**In progress.**

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

Note the user you run the script as should be added to the `dialout` and `tty` groups in order to access the serial port. I've also had problems with Arduino sketches restarting on a serial connection. The Arduino Pro Mini does not seem to do this. To bypass without modifying your Arduino, you can run the [sketch](controller) with the Serial Monitor open.

## REPL Syntax:

* `[primary | secondary] <color>` Sets the primary or secondary color of the LED strip. Secondary is currently unimplemented. To set the strip to red, use one of the following: `primary red`, `primary 255 0 0`, or `primary #ff0000`. Note that Rainbowpy understands HTML5 named colors.
* `dominant` Sets the primary color of the LED strip to the dominant screen color. Not yet implemented.
* `brightness <brightness>` Sets the LED strip brightness. `0..255`.
* `set correction [TypicalSMD5050 | TypicalLEDStrip | Typical8mmPixel | TypicalPixelString | UncorrectedColor]` Sets the color correction of the LED strip.
* `set temperature [Candle | Tungsten40W | Tungsten100W | Halogen | CarbonArc | HighNoonSun | DirectSunlight | OvercastSky | ClearBlueSky | WarmFluorescent | StandardFluorescent | CoolWhiteFluorescent | FullSpectrumFluorescent | GrowLightFluorescent | BlackLightFluorescent | MercuryVapor | SodiumVapor | MetalHalide | HighPressureSodium | UncorrectedTemperature]` Sets the LED color temperature.
* `set transition [immediate | linear | quadratic | dramatic | slow linear | slow quadratic | slow dramatic | subtle]` Sets the transition between colors. Not yet implemented.
* `set mode [pulse | heartbeat | flicker | strobe | throb | solid]` Sets the display mode. Not yet implemented.

Note the REPL supports basic tab completion of commands, but will attempt to do so unintelligently.
