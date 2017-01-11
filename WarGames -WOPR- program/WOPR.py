#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : WOPR.py
#purpose : 'WarGames' game
#detail: It parses user input and looks for the word 'chess' in the answer. Any other response apart from chess results in a user prompt. 
#date : 2016.08.29
#version: 1.0.1
#bugfix:(minor) handles input better. Chess can be in anycase. Still is primitive, we cannot understand context. If the user says 'not chess' or 'anything but chess' it would still take the answer as chess and proceed.



debug = 0;
print("SHALL WE PLAY A GAME? ")

found = 0   ## Flag to indicate 'Chess'/'CHESS'/'chess' found or not
    
while found==0 :
        
    userInput=input()
    listInput = userInput.split(" ")  
    if debug == 1:
        print(listInput)
    for i in range(len(listInput)):
        if listInput[i].lower() =="chess":
            print("Okay " +listInput[i]+ " it is! Thank you!")
            found = 1;
            
    if found ==0: 
        print("Wouldn't you prefer a Good Game of Chess? ")
            
quit()
