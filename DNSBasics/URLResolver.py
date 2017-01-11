#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : file3.py
#date : 2016.10.17
#purpose : DNS resolver: Take either IP or host name and resolve it.
#version: 1.0.0
#features: Handles errors in user input, and excptions. Prints usage and errors/exceptions approprately.

import socket,sys,re

#function to check if argument is passed or not.
def checkArgs():

	if (len(sys.argv) != 2):
		print("\nERROR! Please specify the 'IP or hostname' as argument1 \nUSAGE: " + sys.argv[0] + " [google.com]or[8.8.8.8]\n"   )
		sys.exit()
	return sys.argv[1]

#menu
arg = checkArgs()
#check if the passed argument was IP address [[0-255].0.0.0 format]
match = re.search('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$', arg)

if hasattr(match,'group'):
        try:
            print(socket.gethostbyaddr(arg)[0])
        except socket.error :
            print('IP address not found')
            sys.exit(0)

else:
    try:
        print(socket.gethostbyname(arg))
    except socket.error :
        print('Host name not found.')
        sys.exit(0)
