from machine import Pin

pushbutton1=Pin(19,Pin.IN, Pin.PULL_UP)
led1=Pin(25,Pin.OUT)


import time
import random

tim=None
timmy=None


while True:
    led1.on()
    time.sleep(0.1)
    led1.off()
    time.sleep(0.1)
    val=pushbutton1.value()
    
    if val== 0:
        led1.on()
        time.sleep(2.0)
        led1.off()
        rando_odt = random.randint(1000,5000)
        time.sleep_ms(rando_odt)
        print("starting...")
        led1.on()
        tim=time.ticks_ms()
        while pushbutton1.value()==1:
                pass
        
        timmy=time.ticks_ms()
        timber=time.ticks_diff(timmy,tim)
        led1.off()
        print(timber)
        time.sleep(2.0)#Your Code for making a basic stopwatch using 2 Push Button
