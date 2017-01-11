#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : file3.py
#date : 2016.10.31
#purpose : Pie Chart plot of data read from a csv file. Car Theft data for Rate > 2.5%
#version: 1.0.0

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import csv,os

xaxis =[]
yaxis =[]
rate=[]
production=[]

#function to check if file exists?
def isFile (fileName) :
    if os.path.isfile(fileName):
        return 1
    else:
        return -1


#function to read file and print the req. result
def readCSV(fileName):
    with open('cartheft.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader :
            if row :
                if float(row[4]) >= 2.5: #only if the Rate is > 2.5%
                    #print for validation
                    print (row[1].rjust(20) + row[2].rjust(20) + row[3].rjust(20) +  row[4].rjust(20))
                    xaxis.append(row[1])
                    yaxis.append(row[2])
                    production.append(row[3])
                    rate.append(row[4])

#plot the pie chart function.
def plotPieChart(yaxis):

    # Set figure width to 15 and height to 10
    fig_size = [15.0, 10.0]
    plt.rcParams["figure.figsize"] = fig_size
    yaxis = [int(i) for i in yaxis]
    total = sum(yaxis)
    perc = [(i/total)*100 for i in yaxis]
    labels = xaxis
    cs=cm.Set1(np.arange(40)/40.)
    pie = plt.pie(perc, shadow=True, autopct='%1.1f%%', colors=cs, labels=labels)
    plt.legend(pie[0], labels, loc=(-0.15, 0.6), fontsize=8)
    #plt.pie(perc, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.title("Car Theft Pie Chart", y=1.08)
    plt.axis('equal')
    plt.show()

#main
#check if file exists
if(isFile('cartheft.csv') == -1):
	print ("ERROR! File not found!")
else:
    #print for validation
    print("Model".rjust(20) + "Theft".rjust(20) + "Production".rjust(20) + "Rate".rjust(20))
    print("-"*80)

    readCSV('cartheft.csv')
    plotPieChart(yaxis)
