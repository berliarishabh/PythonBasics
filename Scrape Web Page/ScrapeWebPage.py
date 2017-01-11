#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : ScrapeWebPage.py
#purpose : Scrape page for time
#date : 2016.09.12
#version: 1.0.0 

import urllib.request, re, time
from time import strftime, sleep

#url to scrape data from
url ="http://tycho.usno.navy.mil/timer.html"

#user defined function to scrape data
def scrapePage(url):
    #Open the page and read data and store in a buffer
    page=urllib.request.urlopen(url)
    #Read the page and save the Page data into a string
    pageText=page.read().decode("utf8")
    #Use reg. exp. to find the expression for Timestamp (HH:MM:SS)
    timeMDT= re.search('(\d\d?:\d\d:\d\d\s\w\w\s)(MDT)', pageText)
    timeEDT = re.search('(\d\d?:\d\d:\d\d\s\w\w\s)(EDT)', pageText)
    timeAKDT = re.search('(\d\d?:\d\d:\d\d\s\w\w\s)(AKDT)', pageText)
    #Check to see if search was successfull
    if hasattr(timeMDT,'group'):
        print("\n")
        print("MDT Time: " + timeMDT.group(0) + "\n")
        print("EDT Time: " + timeEDT.group(0) + "\n")
        print("Alaska Time: " + timeAKDT.group(0) + "\n")
    
        print("Current Local Computer Time : " + strftime("%H:%M:%S %p %Z"))
        #Matching for minutes in Local vs Web Page Time(MDT)
        cmpList = timeMDT.group(0).split(":")
        #print (cmpList)
        if not strftime("%M") == cmpList[1] : 
            print ("Local Time of computer is off")
        #One mintue delay 
        sleep(60)
    #if the reg.exp is not found in page, it will give error message
    else :
        print("Time(s) not found at " + url )
        
#Loop always
while 1:
    
    scrapePage(url)
 
quit()    
