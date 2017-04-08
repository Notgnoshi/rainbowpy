#include <FastLED.h>
#include "defines.h"
#include "utils.h"

packet_t packet;

void setup()
{
    memset(&packet, 0, PACKET_SIZE);
    Serial.begin(115200);
    FastLED.addLeds<CHIPSET, DATA_PIN>(leds, NUM_LEDS);

    // our default color correction and temperature
    FastLED.setCorrection(TypicalPixelString);
    FastLED.setTemperature(UncorrectedTemperature);

    // start with nothing lit
    FastLED.clear();
    FastLED.show();
}

void loop()
{
    if (Serial.available() > 0)
    {
        // clear out the packet, and read in a new one
        memset(&packet, 0, PACKET_SIZE);
        Serial.readBytes((char*) &packet, PACKET_SIZE);

        // we've got a packet, now figure out what to do with it
        interpret(packet);
    }
    
    // FastLED.show();
}

