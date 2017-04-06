# colorpy
> Controls an RGB LED strip via serial.

**In progress.**

So far, with an Arduino (with 5V logic) and the RGB LED strip (USC1903 chipset) found [here](https://moderndevice.com/product/serial-rgb-led-strips-ucs1903/). Note that most any addressable RGB LED strip will work -- provided it is supported by the [FastLED](https://github.com/FastLED/FastLED) library. Also depends on [`pyserial`](https://github.com/pyserial/pyserial).

Current usage (requires the [colorize](colorize) sketch to be running on an Arduino):

```
~ $ ./send_colors.py --help
usage: send_colors.py [-h] [--version] [--solid | --led LED] [--device DEVICE] R G B

Controls an RGB LED strip via serial connection with an Arduino

positional arguments:
  R                             RED color value to send 0..255
  G                             GREEN color value to send 0..255
  B                             BLUE color value to send 0..255

optional arguments:
  -h, --help                    show this help message and exit
  --version, -v                 show program's version number and exit
  --solid, -s                   Set strip to solid color. Default.
  --led LED, -l LED             The LED you wish to set
  --device DEVICE, -d DEVICE
                                Serial Device. Defaults to /dev/ttyACM0
```

Note the user you run the script as should be added to the `dialout` and `tty` groups in order to access the serial port. I've also had problems with Arduino sketches restarting on a serial connection. The Arduino Pro Mini does not seem to do this. To bypass without modifying your Arduino, you can run the [sketch](colorize) with the Serial Monitor open.

# TODO:
* Create a simple REPL interpreter for setting the color(s)
    - `set <color>`
    - `set dominant`
    - `set dominant follow`
    - `set off`
    - `set demo`
    - `led <LED> <color>`
    - `transition <color>`
    - `transition led <LED> <color>`
    - `brightness <brightness>`
* Finish figuring out the quickest way to get the dominant color of the screen. See [here](colors).
    - hopefully ignoring whites, grays, and blacks.
    - No need to be deterministic
* `set dominant follow` should run in the background -- returning right back to the interpreter prompt.
* `import readline`
* Will the transition code have to be implemented on the Arduino?
    - hopefully not, all the business logic should go in the same place.
    - Need to worry about saturating the serial connection
* Determine what the Arduino should expect and set that interface in stone.
