#!/usr/bin/env python

import os
import threading
import datetime
import tkinter as tk
import tkinter.font
from tkinter.ttk import *

vidpath = "/home/pi/advent/vids_valentines/"
vidfiles = []
for (root, dirs, files) in os.walk(vidpath, topdown=True):
    for fname in files:
        vidfiles.append(str(os.path.join(root, fname)))

times = []
for i in range(len(vidfiles)):
    loc1 = vidfiles[i].find("_") + 1
    loc2 = vidfiles[i].find(".mp4")
    t = vidfiles[i][loc1:loc2]
    times.append(t)
   
dt = datetime.datetime.today()
d = 10#dt.day
text = "v" + str(d)
fn = "/home/pi/advent/images_valentines/" + str(d) + ".png"

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
    
def playvid():
    print("PLAY MUSIC VIDEO")
    tog = get_tog()
    vidcmnd = "vlc --play-and-exit --qt-minimal-view --fullscreen --no-video-title-show " + vidfiles[tog] # FULLSCREEN
    #vidcmnd = "vlc --play-and-exit --qt-minimal-view " + vidfiles[tog] # FULLSCREEN
    #vidcmnd = "vlc --play-and-exit " + vidfiles[tog] # NOT FULLSCREEN
    os.system(vidcmnd)
    update_tog(tog)
    
def twinkle():
    print("ACTIVATE LIGHTS")
    cmnd2 = "sudo python3 /home/pi/advent/twinkle_hearts.py"
    #os.system(cmnd2)

def Joy():
    t1 = threading.Thread(target=playvid)
    t2 = threading.Thread(target=twinkle)
    t1.start()
    t2.start()
    
    
from tkinter import *
from tkinter import font as tkFont
from tkinter import messagebox
import os

pad = Tk()
helv36 = tkFont.Font(family='Helvetica', size=64, weight='bold')
photo = tk.PhotoImage(file=fn)

pad.attributes('-fullscreen', True)
a = Button(pad, image=photo, text=text, height=480, width=619, fg = "black", bg = "red", command=Joy)
a.place(relx=0.5, rely=0.5, anchor=CENTER)
a['font'] = helv36

pad.mainloop()
