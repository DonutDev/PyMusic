#variables and importing stuff here
import pygame
from pygame import mixer
from tkinter import *
import tkinter as tk
w = tk.Tk()
from tkinter.filedialog import askdirectory
from tkinter import filedialog
path = askdirectory(title='Select Music Folder') # shows dialog box and return the path
w.destroy()
import os
playlist_pos=1
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
def volup():
	mixer.music.set_volume(min(1.0,mixer.music.get_volume()+0.1))
	#mixer.music.play()
def voldown():
	mixer.music.set_volume(max(0.0,mixer.music.get_volume()-0.1))
	#mixer.music.play()
def playAll():
    print("Playing file:")
    playlist_pos=0
    for file in playlist.get(0,END):
    	print("Playing file:")
    	if file.endswith('.mp3'):
    		print("Playing file:", file)
    		playlist.selection_clear(0,END)
    		playlist.selection_set(first=playlist_pos)
    		playlist.activate(playlist_pos)
    		mixer.music.load(file)
    		mixer.music.play()
    		playing_state = True
		    # Wait for the music to play before exiting
    		playlist_pos=playlist_pos+1
    		if playlist_pos>playlist.size()-1:
		       playlist_pos=0
    		while mixer.music.get_busy():
		       pygame.time.Clock().tick(500)

def addfile():
    playlist.insert(playlist_pos,filedialog.askopenfilename())

root=Tk()
root.title('PySong')

mixer.init()
songstatus=StringVar()
songstatus.set("choosing")

#GUI---------------

playlist=Listbox(root,selectmode=SINGLE,bg="#282828",fg="white",font=('arial',15),width=40)
playlist.grid(columnspan=5)

os.chdir(path)
songs=os.listdir()
for s in songs:
    playlist.insert(END,s)


playbtn=Button(root,text="Play",command=playsong)
playbtn.config(font=('Ubuntu',20),bg="grey",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=0)

playbtn=Button(root,text="Play All",command=playAll)
playbtn.config(font=('Ubuntu',20),bg="grey",fg="white",padx=7,pady=7)
playbtn.grid(row=1,column=1)

pausebtn=Button(root,text="Pause",command=pausesong)
pausebtn.config(font=('Ubuntu',20),bg="grey",fg="white",padx=7,pady=7)
pausebtn.grid(row=1,column=2)

stopbtn=Button(root,text="Stop",command=stopsong)
stopbtn.config(font=('Ubuntu',20),bg="grey",fg="white",padx=40,pady=7)
stopbtn.grid(row=1,column=3)

Resumebtn=Button(root,text="Resume",command=resumesong)
Resumebtn.config(font=('Ubuntu',20),bg="grey",fg="white",padx=7,pady=7)
Resumebtn.grid(row=1,column=4)

Loopbtn=Button(root,text="Loop",command=loopsong)
Loopbtn.config(font=('Ubuntu',20),bg="grey",fg="white",padx=25,pady=7)
Loopbtn.grid(row=2,column=4)

VolUp = Button(root ,text = '+',  width = 3, font = ('Times', 10), command=volup)
VolUp.config(font=('Ubuntu',20),bg="grey",fg="white",padx=1,pady=1)
VolUp.grid(row=2,column=0)

VolDown = Button(root ,text = '-',  width = 3, font = ('Times', 10), command=voldown)
VolDown.config(font=('Ubuntu',20),bg="grey",fg="white",padx=1,pady=1)
VolDown.grid(row=2,column=1)

Addbtn=Button(root,text="Add Music",command=addfile)
Addbtn.config(font=('Ubuntu',20),bg="grey",fg="white",padx=7,pady=7)
Addbtn.grid(row=2,column=3)

mainloop()

