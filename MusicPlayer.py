#variables and importing stuff here 
import pygame
from pygame import mixer
from tkinter import *
import tkinter as tk
w = tk.Tk()
from tkinter.filedialog import askdirectory
path = askdirectory(title='Select Music Folder') # shows dialog box and return the path
w.destroy()
import os
#code starts here--------------------------

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("Playing")
    mixer.music.play()

def pausesong():
    songstatus.set("Paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("Stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("Resuming")
    mixer.music.unpause() 
def loopsong():
    songstatus.set("Looping")
    mixer.music.play(loops=-1) 

root=Tk()
root.title('PySong')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#GUI---------------

playlist=Listbox(root,selectmode=SINGLE,bg="DodgerBlue2",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(path)
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)


playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('Ubuntu',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('Ubuntu',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=1)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('Ubuntu',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
stopbtn.grid(row=1,column=2)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('Ubuntu',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=3)

Loopbtn=Button(root,text="Loop",command=loopsong)
Loopbtn.config(font=('Ubuntu',20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
Loopbtn.grid(row=1,column=4)

mainloop()
