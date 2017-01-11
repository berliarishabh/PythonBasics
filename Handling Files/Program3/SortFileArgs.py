#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : SortFileArgs.py
#purpose : A program that takes two	options; a filename	as an argument and a planet	name. i.e. SortFileArgs.py	planetinfo.txt mars
#version: 1.0.0
#features: If the filename specified does not exist, it can handle that and display error message. If the planetname is not in the list it can handle-error
#It also handles the cases of planet-names supplied.


import os, sys


#function to check if file exists?
def isFile (fileName) :
	if os.path.isfile(fileName):
		return 1

	else:
		return -1

#function to read file, find the line with max. length, print length and the line
def readFile(fileName,planetName):

	planets={}
	planetNames=[]
	planetMasses={}
	planetDiameters={}
	planetMoons={}
	planetDistances={}
	planetName = planetName.lower()
	f = open(fileName)
	for line in f:
		(planets['Name'],planets['Mass'],planets['Diameter'],planets['Moon'],planets['Distance'])=line.split()
		planetNames.append(planets['Name'])
		planetMasses[planets['Name']]= float(planets['Mass'])
		planetDiameters[planets['Name']]=float(planets['Diameter'])
		planetMoons[planets['Name']]=int(planets['Moon'])
		planetDistances[planets['Name']]=float(planets['Distance'])

	f.close()
	found = 0
	for i in range(len(planetNames)):
		if(str(planetNames[i])==str(planetName)):
			found=1

	if(found==1):
		print("-"*100)
		print("The information for the planet " + planetName + " is below : ")
		print("Mass".rjust(12) + "Diameter".rjust(12) + "No of Moons".rjust(20) + "Distance from Sun".rjust(20))
		print("-"*100)
		print(format(planetMasses[planetName]).rjust(12) + format(planetDiameters[planetName]).rjust(12) + format(planetMoons[planetName]).rjust(20) + format(planetDistances[planetName]).rjust(20))
	elif(found==0):
		print("Error in Planet Name! Please supply the argument from the list below: [in any case]")
		print(planetNames)

	#function to check if argument is passed or not.
def checkArgs():

	if (len(sys.argv) != 3):
		print("ERROR! Please specify the 'file name' as argument1 and 'Planet Name' as argument2\nUSAGE: " + sys.argv[0] + " filename.txt [planetName]"   )
		sys.exit()
	return sys.argv[1],sys.argv[2]

#main code

#menu
fileName, planetName = checkArgs()

if(isFile(fileName) == -1):
	print ("ERROR! File not found!")
else:
	readFile(fileName, planetName)


quit()
