from rpi_ws281x import *
import time
import os

def get_tog():
    with open("/home/pi/advent/toggle.txt", "r") as f:
        txt = f.readlines()
        f.close()
    tog = int(txt[0])
    return tog

vidpath = "/home/pi/advent/vids/"
vidfiles = []
for (root, dirs, files) in os.walk(vidpath, topdown=True):
    for fname in files:
        vidfiles.append(str(os.path.join(root, fname)))

times = []
for i in range(len(vidfiles)):
    loc1 = vidfiles[i].find("_") + 1
    loc2 = vidfiles[i].find(".mp4")
    t = int(vidfiles[i][loc1:loc2])
    times.append(t)

tog = get_tog()
t = int(times[tog] / 2) + 1
#print(tog)
#print(times[tog])
#print(t)

LED_COUNT = 36
LED_PIN = 21
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
st = 1
dispense = "python3 /home/pi/advent/treat2.py -40 &"

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

for i in range(t):
    
    for x in range(0, LED_COUNT):
        if (x%2) == 0:
            strip.setPixelColor(x, Color(204, 102, 0))
        else:
            strip.setPixelColor(x, Color(127, 0, 255))
    strip.show()
    time.sleep(st)

    for x in range(0, LED_COUNT):
        if (x%2) == 0:
            strip.setPixelColor(x, Color(127, 0, 255))
        else:
            strip.setPixelColor(x, Color(204, 102, 0))
    strip.show()     
    time.sleep(st)
    if i == (t//2):
        os.system(dispense)

for x in range(0, LED_COUNT):
    strip.setPixelColor(x, Color(0, 0, 0))
    strip.show()
