#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : SortFile.py
#purpose : A program that a filename containing planet-info as an argument and sorts it acc. to Mass and Distance from the Sun
#date : 2016.09.25
#version: 1.0.0
#features: If the filename specified does not exist, it can handle that and display error message.

import os, sys


#function to check if file exists?
def isFile (fileName) :
	if os.path.isfile(fileName):
		return 1

	else:
		return -1

#function to read file and print the req. result
def readFile(fileName):

	planets={}
	planetNames={}
	planetMasses={}
	planetDiameters={}
	planetMoons={}
	planetDistances={}

	f = open(fileName)
	for line in f:
		(planets['Name'],planets['Mass'],planets['Diameter'],planets['Moon'],planets['Distance'])=line.split()
		planetMasses[planets['Name']]= float(planets['Mass'])
		planetDiameters[planets['Name']]=int(planets['Diameter'])
		planetMoons[planets['Name']]=int(planets['Moon'])
		planetDistances[planets['Name']]=float(planets['Distance'])

	f.close()
	print("-"*100)
	print("Sorted by Distance from Sun".rjust(60))
	print("Name".rjust(12) + "Mass".rjust(12) + "Diameter".rjust(12) + "No of Moons".rjust(20) + "Distance from Sun".rjust(20))
	print("-"*100)

	for name in sorted(planetDistances, key=planetDistances.get):
	        print(name.rjust(12) + format(planetMasses[name]).rjust(12) + format(planetDiameters[name]).rjust(12) + format(planetMoons[name]).rjust(20) + format(planetDistances[name]).rjust(20))

	print("-"*100)
	print("Sorted by Mass".rjust(50))
	print("Name".rjust(12) + "Mass".rjust(12) + "Diameter".rjust(12) + "No of Moons".rjust(20) + "Distance from Sun".rjust(20))
	print("-"*100)

	for name in sorted(planetMasses, key=planetMasses.get):
		print(name.rjust(12) + format(planetMasses[name]).rjust(12) + format(planetDiameters[name]).rjust(12) + format(planetMoons[name]).rjust(20) + format(planetDistances[name]).rjust(20))

#function to check if argument is passed or not.

def checkArgs():

	if (len(sys.argv) != 2):
		print("ERROR! Please specify the 'file name' as argument1 \nUSAGE: " + sys.argv[0] + " filename.txt"  )
		sys.exit()
	return sys.argv[1]

#main code

#menu
fileName = checkArgs()

if(isFile(fileName) == -1):
	print ("ERROR! File not found!")
else:

	readFile(fileName)


quit()
