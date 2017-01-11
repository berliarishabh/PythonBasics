#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : file2.py
#purpose : Read a file, take the argument for sort, sort the file and print sorted list
#date : 2016.09.19
#version: 1.0.0
#features: If the filename specified does not exist, it can handle that and display error message.
#	   Forward and Reverse order were unclear, so I added Asceding and Desceding sort as well. 
# 	   If a wrong argument is passed, it handles that and diplay error message.

import os, sys


#function to check if file exists?
def isFile (fileName) :
	if os.path.isfile(fileName):
		return 1

	else:
		return -1

#function to read file, find the line with max. length, print length and the line
def readFile(fileName,sortOrder):
	temp = []
	f = open(fileName)
	lines = f.readlines()
	list = [i.strip() for i in lines]
	print("-"*95)
	print ("The original list :\n" + format(list) +"\n")
	if sortOrder == 'desc':
		list.sort(reverse=True)
		print("-"*95)
		print ("The desceding order sorted list :\n" + format(list) +"\n")
	elif sortOrder == 'asc':
		list.sort()
		print("-"*95)
		print ("The asceding sorted list :\n" + format(list) +"\n")
	elif sortOrder == 'forward':
		print("-"*95)
		print ("The forward sorted list :\n" + format(list) +"\n")
	elif sortOrder == 'reverse':
		list.reverse()
		print("-"*95)
		print ("The reverse sorted list :\n" + format(list) +"\n")
	else :
		print("Incorrect Argument passed! Please specify [reverse|forward|asc|desc]")

	f.close()

#function to check if argument is passed or not.

def checkArgs():

	if (len(sys.argv) != 3):
		print("ERROR! Please specify the 'file name' as argument1 and 'sort order' as argument2. \nUSAGE: " + sys.argv[0] + " filename.txt" + " [reverse|forward|asc|desc]" )
		sys.exit()
	return sys.argv[1],sys.argv[2]

#main code

#menu
def printMenu():

	print("*"*95)
	print("You have the following sort options: ")
	print("forward - to sort the file in the forward order, i.e. first element first...")
	print("reverse - to sort the file in the reverse order, i.e. last element first...")
	print("asc - 	 to sort the file in the asceding order")
	print("desc - 	 to sort the file in the desceding order")
	print("*"*95)


fileName, sortOrder = checkArgs()

if(isFile(fileName) == -1):
	print ("ERROR! File not found!")
else:	
	printMenu()
	readFile(fileName, sortOrder)

quit()
