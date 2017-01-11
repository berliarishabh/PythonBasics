#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : file2.py
#date : 2016.10.10
#purpose : On a PLANETS database in sqlite3, return the sorted Table according to the specified column.
#version: 1.0.0
#features: Handles errors in user input like database not present and wrong Usage, prompts the correct USAGE.
#It can also tell if the input sortVar is incorrect and promt to query with correct sortVar
#extra : I have limited the sortVar inputs to mass/distance/name as those were the requirement, but it can actually sort based on all table columns.

import os, sys, sqlite3

#function to check if file exists?
def isFile (fileName) :
	if os.path.isfile(fileName):
		return 1

	else:
		return -1

#function used to initally create and insert into databases
def insertRecord(db, id, name, mass, diameter, moons, distance ):
	query = "insert into planets (id, name, mass, diameter, moons, distance) values (?,?,?,?,?,?)"
	t = (id, name, mass, diameter, moons, distance,)
	cursor = db.cursor()
	cursor.execute(query,t)
	db.commit()

#function used to query the database
def queryResults(db, sortVar):
	#limitaton on the sortVar as per requirements
	list = ['distance', 'name', 'mass']
	if sortVar.lower() in list :
		query = "select * from planets order by " + sortVar +""
		cursor = db.cursor()
		cursor.execute(query)
		rows = cursor.fetchall()
		print("\nThe planet information sorted in order of planet " + sortVar.upper() + "\n")
		print("No".rjust(12) + "Name".rjust(12) + "Mass".rjust(12) + "Diameter".rjust(12) + "No of Moons".rjust(20) + "Distance from Sun".rjust(20))
		for row in rows:
			print(row[0].rjust(12) + row[1].rjust(12) + format(row[2]).rjust(12) + format(row[3]).rjust(12) + format(row[4]).rjust(12) + format(row[5]).rjust(24) )
		print("\n")
	else :
		print("\nError! Please specify the sort order out of the following options : (mass|distance|name)\n")

#function to check if arguments are passed correctly or not.
def checkArgs():

	if (len(sys.argv) != 3):
		print("ERROR! Please specify the 'database name' as argument1 and 'Sort by[distance|mass|alphabetically]' as argument2\nUSAGE: " + sys.argv[0] + " planetsDB.sql3 (mass)|(distance)|(name)"   )
		sys.exit()
	return sys.argv[1],sys.argv[2]

#main code

#menu
fileName, sortVar = checkArgs()


if(isFile(fileName) == -1):
	print ("ERROR! File not found!")
else:
	db = sqlite3.connect(fileName)
	db.row_factory = sqlite3.Row
	queryResults(db,sortVar)


quit()
