#Written by Lucas Giertz
#Quelle zum Bild : http://feuerwehr-schapbach.de/wp-content/uploads/2015/01/blaulicht-250x250.gif

#!/usr/bin/python

import sys
import os
import Tkinter
import tkMessageBox
top = Tkinter.Tk()


def aCallBack():
	os.system('python relayoff.py')
	
def nCallBack():
	os.system('python relayon.py')

img = Tkinter.PhotoImage(file="123.gif")
w = Tkinter.Label(top, text="Blaulicht Control", image=img)
B = Tkinter.Button(top, text="AN", command = nCallBack)
A = Tkinter.Button(top, text="OFF", command = aCallBack)

w.photo = img
w.pack()
B.pack()
A.pack()
top.mainloop()
