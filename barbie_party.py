# Write your code here :-)
#code for PWM
#code for neopixels, motor
import machine
from machine import Pin
from neopixel import NeoPixel
import time
import math

#import servo for motor

class Servo:
    def __init__(self,pin_id,min_us=544.0,max_us=2400.0,min_deg=0.0,max_deg=180.0,freq=50):
        self.pwm = machine.PWM(machine.Pin(pin_id))
        self.pwm.freq(freq)
        self.current_us = 0.0
        self._slope = (min_us-max_us)/(math.radians(min_deg)-math.radians(max_deg))
        self._offset = min_us

    def write(self,deg):
        self.write_rad(math.radians(deg))

    def read(self):
        return math.degrees(self.read_rad())

    def write_rad(self,rad):
        self.write_us(rad*self._slope+self._offset)

    def read_rad(self):
        return (self.current_us-self._offset)/self._slope

    def write_us(self,us):
        self.current_us=us
        self.pwm.duty_ns(int(self.current_us*1000.0))

    def read_us(self):
        return self.current_us

    def off(self):
        self.pwm.duty_ns(0)

# defining sensor, pixels and motor pins
mysensor= Pin(33, Pin.IN)
dataPin = 15
pixels = 16
purp = (255,0,255)
np = NeoPixel(Pin(dataPin, Pin.OUT), pixels)
my_servo= Servo(pin_id=4)

# purple light glowing
for i in range (pixels) :
    np[i]= purp
np.write()

#condition for turning off motor when light glows
while True:
    sense=mysensor.value()
    #when light is shining, motor moves
    while sense==1:
        my_servo.write(0)
        time.sleep(0.1)
        my_servo.write(30)
        time.sleep(0.1)
        sense=mysensor.value()
    #when light is blocked out, it stops
    my_servo.write(0)



