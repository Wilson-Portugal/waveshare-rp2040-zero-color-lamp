# blinky.py
# written for Waveshare RP2040 Zero
# Wilson Portugal, Lisboa, Portugal
# 25 February 2023

from neopixel_value import neo_pixel
from utime import  sleep

counter = 0
while counter < 5:
    neo_pixel((1,0,0)) # red - vermelha
    sleep(1)
    neo_pixel((0,1,0)) # green - verde
    sleep(1)
    neo_pixel((0,0,1)) # blue - azul
    sleep(1)
    counter = counter + 1
    
neo_pixel(0)
