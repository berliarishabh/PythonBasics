#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : file1.py
#purpose : Read a file, find the longest line, print both length and line
#date : 2016.09.19
#version: 1.0.0
#features: If the filename specified does not exist, We can handle the Error

import os, sys


#function to check if file exists?
def isFile (fileName) :
	if os.path.isfile(fileName):
		return 1

	else:
		return -1

#function to read file, find the line with max. length, print length and the line
def readFile(fileName):
	temp = []
	f = open(fileName)
	lines = f.readlines()
	list = [i.strip() for i in lines]
	for l in list:
		temp.append(len(l))
	length = max(temp)
	for i,j in enumerate(temp) :
		if j == length :
			index = i
	print("The length of the longest line is : " + format(length) )
	print("The longest line is : " + list[index])
	f.close()

#function to check if argument is passed or not.

def checkArgs():

	if (len(sys.argv) != 2):
		print("ERROR! Please specify the file name as argument. \nUSAGE: " + sys.argv[0] + " filename.txt" )
		sys.exit()
	return sys.argv[1]

#main code

fileName = checkArgs()

if(isFile(fileName) == -1):
	print ("ERROR! File not found!")
else:
	readFile(fileName)

quit()
