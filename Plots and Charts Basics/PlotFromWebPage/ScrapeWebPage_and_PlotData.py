#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : ScrapeWebPage_and_PlotData.py
#date : 2016.11.7
#purpose : Scrape the .census.gov page for the CSV data, print the line graph of Observed vs Estimated Population with Legend.
#version: 1.0.0


import requests
import csv
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable


def readCSVtoLists():
    observerPop =[]
    predictedPop =[]
    states=[]



    url = "http://www.census.gov/popest/data/counties/totals/2011/tables/CO-EST2011-01-08.csv"
    try:
        r = requests.get(url)
        text = r.text
        reader = csv.reader(text.splitlines(), delimiter=',')
        for row in reader :
            if row:
                    observerPop.append(row[2])
                    predictedPop.append(row[3])
                    states.append(row[0])

        del observerPop[:4]
        del observerPop[-6:]
        del predictedPop[:4]
        del predictedPop[-6:]
        del states[:4]
        del states[-6:]

        predictedPop = [i.replace(',', '') for i in predictedPop]
        observerPop = [i.replace(',', '') for i in observerPop]
        states = [i.replace('.', '') for i in states]

        predictedPop = [int(i) for i in predictedPop]
        observerPop = [int(i) for i in observerPop]

        return observerPop,predictedPop,states
    except requests.exceptions.RequestException:  # This is the correct syntax
        print("Error with the Request! Please Try Again!")
        sys.exit(1)

def plotGraph(predictedPop,observerPop,states):
    fig_size = [12.0, 9.0]
    plt.rcParams["figure.figsize"] = fig_size
    plt.plot(predictedPop,color='red')
    plt.plot(observerPop, color='blue')
    groups=len(predictedPop)
    index = np.arange(groups)
    plt.title("Observed Vs. Predicted Population of Colorado and its Counties")
    plt.xticks(index, states, rotation='vertical' )
    plt.margins(0.025)
    plt.xlabel("Name of Counties")
    plt.ylabel("Population")
    plt.legend(['Observed Population','Estimated Population'], loc='upper right')
    plt.tight_layout()
    plt.show()

def printTable(predictedPop,observerPop,states):
    table = PrettyTable()
    table.add_column("Name of County/[State]", states)
    table.add_column("Obsevered Population", observerPop)
    table.add_column("Predicted Population", predictedPop)
    print (table)

if __name__ == '__main__':
    try:
        print("Requesting .csv file and parsing it....")
        predictedPop,observerPop,states=readCSVtoLists()
        print("Printing Table data....")
        printTable(predictedPop,observerPop,states)
        print("Plotting Graph...")
        plotGraph(predictedPop,observerPop,states)
    except Exception as e:
        print ("Error! Please try again")
        print ("Error message : ",e)
