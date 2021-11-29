#!/usr/bin/env python3
from os import truncate
import re

from ev3dev.core import Led, Screen
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev.ev3 import Button, ColorSensor
from time import sleep

"""def calibrate():
    r = 0
    t = True
    lcd.clear()
    lcd.draw.text((2,26), "Poloz robota na bialym tle")
    lcd.update()
    sleep(2)
    while t:
        if bnt.any():
            cl.mode = 'COL-REFLECT'
            white = cl.value()
            lcd.clear()
            lcd.draw.text((2,26), "Poloz robota na bialym tle")
            lcd.update()
            sleep(2)
            if bnt.any():
                black = cl.value()
                r = (white + black)/2
                t = False
            else:
                sleep(0.01)
        else:
            sleep(0.01)
    return r"""


def calibrate():
    cl.mode = 'COL-REFLECT'
    print("Na bialy 5 s")
    input("")
    white = cl.value()
    print("Na czanry 5 s")
    input("")
    black = cl.value()
    r = (white + black) / 2
    return r


def regulator(e):
    cl.mode = 'COL-REFLECT'
    return 100 * e


cl = ColorSensor()
left = LargeMotor(OUTPUT_B)
right = LargeMotor(OUTPUT_C)
lcd = Screen()
bnt = Button()
right.stop()
left.stop()
r = calibrate()
red = 0
print("Przenies robota")
sleep(10)
while red < 1:
    print("Jade")
    cl.mode = 'COL-REFLECT'
    y = cl.value()
    e = r - y
    alfa = 125
    if e < 0:
        left.run_forever(speed_sp=50)
        right.run_forever(speed_sp=50 + alfa)
    else:
        left.run_forever(speed_sp=50 + alfa)
        right.run_forever(speed_sp=50)
    cl.mode = 'COL-COLOR'
    print(cl.value())
    if cl.value() == 5:
        red += 1

right.stop()
left.stop()
print("Skonczylem jazde")
colors = ('unknown', 'black', 'blue', 'green', 'yellow', 'red', 'white', 'brown')
