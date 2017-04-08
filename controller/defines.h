#ifndef DEFINES_H_
#define DEFINES_H_

#include <FastLED.h>

#define NUM_LEDS 50
#define DATA_PIN 13
#define CHIPSET UCS1903

CRGB leds[NUM_LEDS];

struct packet_t
{
    // what kind of goodies lies in `data`
    uint8_t type;
    // the packet_t payload
    uint8_t data[3];
};

struct rgb_t
{
    uint8_t red;
    uint8_t green;
    uint8_t blue;
};

const size_t PACKET_SIZE = sizeof(packet_t);

// possible packet types --> tells us how to interpret the data portion of the struct
#define SET_PRIMARY_COLOR 10
#define SET_SECONDARY_COLOR 20
#define SET_BRIGHTNESS 30
#define SET_TRANSITION 40
#define SET_MODE 50
#define SET_COLOR_CORRECTION 60
#define SET_COLOR_TEMPERATURE 70

const LEDColorCorrection corrections[5] =
{
    TypicalSMD5050,
    TypicalLEDStrip,
    Typical8mmPixel,
    TypicalPixelString,
    UncorrectedColor,
};

const ColorTemperature temperatures[20] =
{
    Candle,
    Tungsten40W,
    Tungsten100W,
    Halogen,
    CarbonArc,
    HighNoonSun,
    DirectSunlight,
    OvercastSky,
    ClearBlueSky,
    WarmFluorescent,
    StandardFluorescent,
    CoolWhiteFluorescent,
    FullSpectrumFluorescent,
    GrowLightFluorescent,
    BlackLightFluorescent,
    MercuryVapor,
    SodiumVapor,
    MetalHalide,
    HighPressureSodium,
    UncorrectedTemperature,
};

#endif /* end of include guard: DEFINES_H_ */
