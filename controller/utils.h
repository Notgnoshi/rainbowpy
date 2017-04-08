#ifndef UTILS_H_
#define UTILS_H_

#include "defines.h"
#include <FastLED.h>

// functions defined in this header
void interpret(packet_t packet);

void interpret(packet_t packet)
{
    switch (packet.type)
    {
    // I don't know how to handle secondary color yet, so it will do the same as the primary color.
    case SET_SECONDARY_COLOR:
    case SET_PRIMARY_COLOR:
        rgb_t rgb;
        memcpy(&rgb, packet.data, 3);
        // my LED strip thinks blue is actually green...
        fill_solid(leds, NUM_LEDS, CRGB(rgb.red, rgb.blue, rgb.green));
        FastLED.show();
        break;
    case SET_BRIGHTNESS:
        FastLED.setBrightness(packet.data[0]);
        FastLED.show();
        break;
    case SET_TRANSITION:
        break;
    case SET_MODE:
        break;
    case SET_COLOR_CORRECTION:
        FastLED.setCorrection(corrections[packet.data[0]]);
        FastLED.show();
        break;
    case SET_COLOR_TEMPERATURE:
        FastLED.setTemperature(temperatures[packet.data[0]]);
        FastLED.show();
        break;
    default:
        break;
    }
}


#endif /* end of include guard: UTILS_H_ */
