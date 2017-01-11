#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : file1.py
#purpose : Random number guessing game - simple
#date : 2016.08.29
#version: 1.1.0 
#bugfixes: It handles input conditions better. Can handle string inputs now and return error. If error in number the game Restarts and new random number is genreated. 


debug= 1# debug = 1 for printing debug statements
import random
minNumber = 1
maxNumber = 20
while 1 : 
    print("\nWelcome to the Random Number Guessing game! Press enter! ")
    input()
    randomNum = random.randint(minNumber,maxNumber)
    if debug==1 :
        print(randomNum) ## Debug statement
    
    print("The Random number has been generated! Lets Play!\n")
    userInput = input("Guess the number (between 1-20) ? ")
    
    if userInput.isdigit() :
        userInput = int(userInput)     
        while userInput != randomNum:
                
            if userInput<randomNum :
                print("Your guess is lower! Go up!")
                
            elif userInput>maxNumber :
                print("Guess exceeds the range!")
            
            elif userInput > randomNum :
                print("Your guess is higher! Go down!")
                
            userInput = input("Guess the number again? ")
            if userInput.isdigit() :
                userInput = int(userInput)
            else:
                print("Error in Input! Please only enter a postive Integer.")
                break
        if(userInput==randomNum) :
            print("The guess was spot on!")
    else :
        print("Error! in the Input. Enter a Positive Integer in range.")    
quit()
