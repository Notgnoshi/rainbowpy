#include <FastLED.h>

#define NUM_LEDS 50
#define DATA_PIN 13
#define CHIPSET UCS1903
#define PACKET_SIZE 5

CRGB leds[NUM_LEDS];

struct packet_t
{
    uint8_t solid;
    uint8_t LED;
    uint8_t red;
    uint8_t green;
    uint8_t blue;
};

// global buffer to read data into
uint8_t input[PACKET_SIZE] = {0};
packet_t data;

void set_color(packet_t data);


void setup()
{
    Serial.begin(115200);
    FastLED.addLeds<CHIPSET, DATA_PIN>(leds, NUM_LEDS);
    FastLED.clear();
    FastLED.show();
}


void loop()
{
    if (Serial.available() > 0)
    {
        memset(input, 0, PACKET_SIZE);
        memset(&data, 0, PACKET_SIZE);

        Serial.readBytes((char*) input, PACKET_SIZE);
        memcpy(&data, input, PACKET_SIZE);

        char response[256] = "";
        sprintf(response, "solid: %d LED: %d R: %d G: %d B: %d", data.solid, data.LED, data.red, data.green, data.blue);
        Serial.println(response);
        set_color(data);
    }
}


void set_color(packet_t data)
{
    if (data.solid >= 1)
    {
        fill_solid(leds, NUM_LEDS, CRGB(data.red, data.blue, data.green));
        FastLED.show();
    } else {
        leds[data.LED].setRGB(data.red, data.blue, data.green);
        FastLED.show();
    }
}


