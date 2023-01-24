from time import sleep
from pimoroni import Button
from machine import Pin

button_a = Button(7, invert=False)
button_b = Button(8, invert=False)
button_c = Button(9, invert=False)
button_up = Button(22, invert=False)
button_down = Button(6, invert=False)

led = Pin(25, Pin.OUT)

while True:
    if button_up.is_pressed:
        led.value(1)
    if button_down.is_pressed:
        led.value(0)
    sleep(0.1)