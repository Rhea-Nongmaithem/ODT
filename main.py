# Write your code here :-)
#import modules
#set up bend sensor
#set up ADC
#set up neopixel
# while True loop
#read ADC vales
#if value in a certain range: light glows from red to green (255,0,0) then to (0,255,0) and diff ranges
#turn on leds one by one

from machine import Pin, ADC
from neopixel import NeoPixel
import time

dataPin = 5
pixels=16

thresh = 700
#colours:
Blue=(57,225,20)
Red=(225,20,32)

np=NeoPixel(Pin(dataPin, Pin.OUT), pixels)
adc = ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)

while True:
    bent_val= adc.read()
    print(bent_val) #bent_val =2119

    if bent_val>thresh+20:
        print("yes")
        for i in range(pixels):
            np[i] = Blue
            time.sleep(0.05)
            np[i]=(0,0,0)
            np.write()
            time.sleep(0.01)
    elif bent_val<thresh-20:
        for i in range(pixels):
            np[i] = Red
            np.write()
            time.sleep(0.05)
            np[i]=(0,0,0)
            np.write()
            time.sleep(0.01)
    else:
        for i in range(pixels):
            np[i] = (0,0,0)
            np.write()
