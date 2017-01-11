#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : file1-client.py
#date : 2016.10.17
#purpose : Simple UDP client to send messages to server
#version: 1.0.0
#features: Handles errors in user inputs and prompts the correct USAGE and error code.
#use of try except for better error handling.


import sys,socket

#function to check if argument is passed or not.
def checkArgs():

	if (len(sys.argv) != 4):
		print("\nERROR! Please specify the 'Server IP' as argument1, 'Port' as argument2, 'Message' as argument3\nUSAGE: " + sys.argv[0] + " 127.0.0.1 [>1024] 'Hello World'\n"   )
		sys.exit()
	return sys.argv[1],int(sys.argv[2]),sys.argv[3]


#menu
serverIP, port, message = checkArgs()
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as msg:
    print('Error in creating socket')
    print ('\nError Code : ' + str(msg[0]) + ' \nError Message: ' + msg[1])
    sys.exit()

data = message.encode('ascii')

try :
    sock.sendto(data, (serverIP,port))
except socket.error as msg:
        print('Error in sending data')
        print('Error Code : ' + str(msg[0]) + ' Error Message ' + msg[1])
        sys.exit()


quit()
