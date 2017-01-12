#!/usr/bin/env python3
#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : GUIBasics.py
#date : 2016.11.18
#purpose : Using Tkinter create a simple GUI, have 3 buttons to do different tasks; 1. Get IP of www.colorado.edu, Get Title from page www.colorado.edu and 3.Quit the program
#version: 1.0.0
#features: Error handling, with try and except

from tkinter import *
from bs4 import BeautifulSoup
import socket,requests

#funtion to close window
def endWindow():
    root.destroy()

#function to get IP
def getIP(arg):

    try:
        p = "IP : \n"
        p += format(socket.gethostbyname(arg))
        display.configure(text=p)
    except socket.error :
        p = "Host name not found."
        display.configure(text=p)

#function to get Title from hostname.
def getTitle(arg):

    try:
        soup = BeautifulSoup(requests.get(arg).text,"lxml")
        #.string to strip of the html tags.
        p = "Title : \n"
        p += soup.title.string
        display.configure(text=p)
    except Exception as e:
        p = e
        display.configure(text=p)

#create window
root=Tk()

#set window size
root.geometry('480x240')

#Label to print output on screem
Label(root, text = "HW10 GUI").grid(row=1, column=2, columnspan=1, ipadx="180")
Label(root, text = "_"*50).grid(row=6,column=1,columnspan=5)
display = Label(root,text="")
display.grid(row=9, column=2, columnspan=1)

buttonA=Button(root, text="Get IP (www.colorado.edu)", command=lambda:getIP("www.colorado.edu")).grid(row=2,column=2)
buttonB=Button(root, text="Get Page Title (www.colorado.edu)", command=lambda:getTitle("http://www.colorado.edu")).grid(row=3,column=2)
buttonC=Button(root, text="End Program", command=lambda:endWindow()).grid(row=4,column=2)

#open the window
root.mainloop()
