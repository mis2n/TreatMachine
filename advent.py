import os
import time
import threading
import datetime
import tkinter as tk
import tkinter.font
from tkinter.ttk import *

dt = datetime.datetime.today()
d = dt.day
m = dt.month
text = ""
print(dt, "*", d, "*", m)

fn = "/home/pi/advent/day_images/h" + str(d) + ".png"
vidpath = "/home/pi/advent/vidshalloween/"
cmnd2 = "sudo python3 /home/pi/advent/twinkle_spooky.py"

'''

if m == 2:
    fn = "/home/pi/advent/day_images/v" + str(d) + ".png"
    vidpath = "/home/pi/advent/vidsvalentines/"
    cmnd2 = "sudo python3 /home/pi/advent/twinkle_hearts.py"
if m == 3:
    fn = "/home/pi/advent/day_images/p" + str(d) + ".png"
    #fn = "/home/pi/advent/day_images/p15.png"
    vidpath = "/home/pi/advent/vidspatricks/"
    cmnd2 = "sudo python3 /home/pi/advent/twinkle_clovers.py"
if m == 10:
    fn = "day_images/h" + str(d) + ".png"
    vidpath = "vidshalloween/"
    cmnd2 = "sudo python3 twinkle_spooky.py"
if m == 12:
    fn = "day_images/" + str(d) + ".png"
    vidpath = "vids/"
    cmnd2 = "sudo python3 twinkle.py"
'''
print(fn, "***********************************************")
print("vidpath", vidpath)
print("twinkle command", cmnd2)    
# get list of video files available
vidfiles = []
for (root, dirs, files) in os.walk(vidpath, topdown=True):
    for fname in files:
        vidfiles.append(str(os.path.join(root, fname)))
print("got video list", len(vidfiles))        
# Get run-time of each video
times = []
for i in range(len(vidfiles)):
    loc1 = vidfiles[i].find("_") + 1
    loc2 = vidfiles[i].find(".mp4")
    t = vidfiles[i][loc1:loc2]
    times.append(t)
print("got video lengths", len(times))
# Find out which video was played last, return tog value of next video to play
def get_tog():
    with open("/home/pi/advent/toggle.txt", "r") as f:
        txt = f.readlines()
        f.close()
    tog = int(txt[0])
    return tog

def update_tog(tog):
    if tog < len(vidfiles)-1:
        tog += 1
    else:
        tog = 0
    with open("/home/pi/advent/toggle.txt", "w") as f:
        f.write(str(tog))
        f.close()
        
# function to play video in full-screen mode using VLC media player
def playvid():
    print("PLAY MUSIC VIDEO")
    tog = get_tog()
    vidcmnd = "vlc --play-and-exit --qt-minimal-view --fullscreen --no-video-title-show " + vidfiles[tog] # FULLSCREEN
    #vidcmnd = "vlc --play-and-exit --qt-minimal-view " + vidfiles[tog] # FULLSCREEN
    #vidcmnd = "vlc --play-and-exit " + vidfiles[tog] # NOT FULLSCREEN
    os.system(vidcmnd)
    update_tog(tog)

# Function that runs LED lightshow code (os command must use sudo to access GPIO pins)
def twinkle():
    print("ACTIVATE LIGHTS")
    cmnd2 = "sudo python3 /home/pi/advent/twinkle_spooky.py"
    os.system(cmnd2)

# Function that runs candy dispenser (not currently in use)
def Joy():
    t1 = threading.Thread(target=playvid)
    t2 = threading.Thread(target=twinkle)
    t1.start()
    t2.start()
    time.sleep(30)
    
from tkinter import *
from tkinter import font as tkFont
from tkinter import messagebox
print("creating GUI")
# Creating GUI window
pad = Tk()
helv36 = tkFont.Font(family='Helvetica', size=64, weight='bold')
photo = tk.PhotoImage(file=fn)
# Comment out line below for testing
pad.attributes('-fullscreen', True)
a = Button(pad, image=photo, text=text, height=480, width=619, fg = "black", bg = "red", command=Joy)
a.place(relx=0.5, rely=0.5, anchor=CENTER)
a['font'] = helv36

# Launch GUI
pad.mainloop()
