#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : BarGraph.py
#date : 2016.10.31
#purpose : Bar Graph plot of data read from a csv file. Population vs States
#version: 1.0.0

import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter
import numpy as np
import csv,os

xaxis =[]
yaxis =[]

#function to check if file exists?
def isFile (fileName) :
    if os.path.isfile(fileName):
        return 1
    else:
        return -1

#function to read file and print the req. result
def readCSV(fileName):

    with open('statepop.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader :
            if row :
                #print for validation
                print (row[0].rjust(20) + row[1].rjust(20))
                xaxis.append(row[0])
                yaxis.append(row[1])

#barGraph plot function
def plotBarGraph(yaxis):

    fig_size = [12.0, 9.0]
    plt.rcParams["figure.figsize"] = fig_size
    yaxis = [int(i) for i in yaxis]
    groups=len(yaxis)
    index = np.arange(groups)
    barWidth = 0.8
    plt.bar(index, yaxis, barWidth, color='blue')
    plt.xlabel("States")
    plt.ylabel("Population")
    plt.title(" Population Bar Graph")
    plt.xticks(index + barWidth, xaxis, rotation='vertical' )
    plt.tight_layout()

    #ax = plt.gca()
    #ax.yaxis.set_major_formatter(FormatStrFormatter('%.0f'))
    plt.show()


#main
if(isFile('statepop.csv') == -1):
	print ("ERROR! File not found!")
else:
    print("State".rjust(20) + "Population".rjust(20))
    print("-"*50)
    readCSV('statepop.csv')
    plotBarGraph(yaxis)
