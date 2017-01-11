#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : file1.py
#date : 2016.10.10
#purpose : On a states database in sqlite3, return the stateName when the correct stateAbbr is passed.
#version: 1.0.0
#features: Handles errors in user input like database not present and wrong Usage, prompts the correct USAGE.
#It can also tell if the input stateAbbr is incorrect and promt to query with correct stateAbbr

import os, sys, sqlite3

#function to check if file exists?
def isFile (fileName) :
	if os.path.isfile(fileName):
        return 1
	else:
        return -1

#function used to initally create and insert into databases
def insertRecord(db, id, stateName, stateAbbr):
	query = "insert into states (id, stateName, stateAbbr) values (?,?,?)"
	t = (id, stateName, stateAbbr,)
	cursor = db.cursor()
	cursor.execute(query,t)
	db.commit()

#function used to query the database
def queryResults(db, stateAbbr):
	query = "select stateName from states where stateAbbr=?"
	t = (stateAbbr.upper(),)
	cursor = db.cursor()
	cursor.execute(query,t)
	rows = cursor.fetchall()
	if rows:
		for row in rows:
			print("The name of the State is : " + row[0])
	else :
		print("\nWrong State Abbreviation specified. Please specify a correct 2 letter abbreviation eg. WY \n")

#function to check if argument is passed or not.
def checkArgs():

	if (len(sys.argv) != 3):
		print("\nERROR! Please specify the 'database name' as argument1 and '2 letter state abbreviation' as argument2\nUSAGE: " + sys.argv[0] + " statesdb.sql3 stateAbbr(XX)\n"   )
		sys.exit()
	return sys.argv[1],sys.argv[2]

#main code

#menu
fileName, stateAbbr = checkArgs()



if(isFile(fileName) == -1):
	print ("\nERROR! File not found!\n")
else:
	db = sqlite3.connect(fileName)
	db.row_factory = sqlite3.Row
	queryResults(db, stateAbbr)



quit()
