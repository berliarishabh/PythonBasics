#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : GuessSeconds.py
#purpose : Seconds of time guessing program
#date : 2016.09.12
#version: 1.0.0 
import time
from time import strftime

#user defined function to guess time
def guessTime(guess):

    if(int(strftime("%S")) == int(guess)):
        return 1
    else :
        return 0

#main program
userInput = input("\nEnter a number between 1 and 59 : ")

count = 0
while count!=5:

    if guessTime(userInput)==1:
        print ("\nMatch")
        break
    else :
        userInput = input("\nWrong! Try again : ")
        count +=1 
if not(guessTime(userInput)) : 
    print("\nNo Match")
    
quit()


