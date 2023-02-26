# waveshare-rp2040-zero-color-lamp

I purchased a **Raspberry Pi Pico clone** off of **AliExpress**, the **Waveshare RP2040 Zero**, because of its small form size and fairly cheap price. I plugged it into my **Chromebook**, with Crostini installed, while holding down the **BOOT** button. I downloaded the most recent **Raspberry Pi PICO micropython firmware** (rp2-pico-20230224-unstable-v1.19.1-896-g2e4dda3c2.uf2) and copied it to the device. I went to my command line and issued `ls -l /dev/ttyACM*` command to make sure that it showed up. It was all good. I opened up my **Thonny IDE** and nice, all was good. No files are on the device. I grab the default **Blinky.py** file from the **Raspberry Pi PICO repository** and I find that the LED, if it is there, is not standard to the **PICO**. 

So, all of that being as it is, I found datasheets from the [Waveshare website](https://www.waveshare.com/rp2040-zero.htm). I found that this device comes with a WS2812 RGB color LED array. Cool! So I have seen something like this before and I really never did dig too much into it. But to have it on such a small form factor RP2040 device.

So, I looked around and I found a reference on [Mondogeo's GitHub Page](https://github.com/Mondogeo). Simple yet nice. I made my **blinky.py** work. So, I publish my stuff here if it be of help to anyone else.

This video shows my Waveshare RP2040 Zero connected to a USB-C dongle running from my laptop and running through the **blinky.py** routine.

https://user-images.githubusercontent.com/108299098/221413937-980aae3e-fe99-4bea-b0d5-d748cdc215b7.mp4

