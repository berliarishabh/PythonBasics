#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : PlotPing.py
#date : 2016.11.7
#purpose : ping 8.8.8.8 and 4.2.2.1 and plot the line graphs for their reponse times, also use prettytable to plot the data point table.
#save and show plot if 'filename.png is filename is provided, else just show the plot.'
#version: 1.0.0

import subprocess
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import sys

def pingIP(ip):
    #run the file
    with open('output.txt','w') as out:
        out.write(subprocess.check_output(['ping','-c','50', ip],stderr=subprocess.STDOUT,universal_newlines=True))

    pingList=[]
    #open the File and read line by line, while appending the the time(ms) to a list
    with open('output.txt','r') as out:
        for line in out:
            try:
                pingList.append((line.split('=')[-1].split()[0]))

            except Exception as e:
                break;
                print ("Error")
    #Fix the List , Remove 'PING' from the list.
    del pingList[:1]
    subprocess.call(['rm','-r','output.txt'])
    #pingList=[float(i) for i in pingList]
    return pingList

def printTable(ip1,ip2):
    table = PrettyTable()
    table.add_column("Time(ms) for 8.8.8.8", ip1)
    table.add_column("Time(ms) for 4.2.2.1", ip2)
    print (table)


def plotGraph(ip1,ip2):
    fig_size = [12.0, 9.0]
    plt.rcParams["figure.figsize"] = fig_size
    plt.plot(ip1, color='red')
    plt.plot(ip2, color='blue')
    plt.title("PING time(ms) comparison for 8.8.8.8 and 4.2.2.1 for 50 tries.")
    plt.margins(0.025)
    plt.xlabel("PING (0-49)")
    plt.ylabel("Time(ms)")
    plt.legend(['8.8.8.8','4.2.2.1'], loc='upper right')
    plt.tight_layout()



#function to check if file name is passed or not, if passed return the filename else return 0.

def checkArgs():
    if (len(sys.argv) == 2):
        return sys.argv[1]
    else :
        return 0

#main
if __name__ == '__main__':

    try:
        filename=checkArgs()
        if (filename== 0) :
            print("Output File would not be saved! If you want to save the output plot, please provide the Name of file as argument without extension.\nIt would be saved with .png [USAGE: file2.py filename]")
            print("Pinging IPs...")
            ip1 = pingIP('8.8.8.8')
            ip2 = pingIP('4.2.2.1')
            print("Printing Table Data...")
            printTable(ip1,ip2)
            print("Plotting Graph Data...")
            plotGraph(ip1,ip2)
            plt.show()

        else :
            print("Output File is being generated and would be saved as " + filename +".png, Hold on!")
            print("Pinging IPs...")
            ip1 = pingIP('8.8.8.8')
            ip2 = pingIP('4.2.2.1')
            print("Printing Table Data...")
            printTable(ip1,ip2)
            print("Plotting Graph Data...")
            plotGraph(ip1,ip2)
            print("Saving File! : /" + filename +".png")
            plt.savefig(filename+'.png')
            plt.show()

    except Exception as e:
        print ("Error! Please try again")
        print ("Error message : ",e)
