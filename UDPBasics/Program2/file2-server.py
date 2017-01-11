#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : file2-server.py
#date : 2016.10.17
#purpose : UDP server to recieve file and compute the sha256 of the file and transmit that back to the client.
#version: 1.0.0
#features: Handles errors in user inputs like wrong port specified or port already in use, prompts the correct USAGE and error code.
#use of try except for better error handling.

import sys,socket,hashlib

#function to compute and return the sha256 of file
def printSHA256(fileName) :

    hash = hashlib.sha256()
    with open (fileName, 'rb') as f :
        buffer = f.read()
        hash.update(buffer)
        print('The SHA256 of file is: ' + hash.hexdigest())
        return hash.hexdigest()

#function to check if argument is passed or not.
def checkArgs():

	if (len(sys.argv) != 2):
		print("\nERROR! Please specify the 'Port' as argument1 \nUSAGE: " + sys.argv[0] + " [>1024]\n"   )
		sys.exit()
	return int(sys.argv[1])

#function to recieveFile from the client.
def recieveFile():

    f = open("recieved",'wb')
    data,addr = sock.recvfrom(1024)

    try:
        while(data):
            f.write(data)
            sock.settimeout(2)
            data,addr = sock.recvfrom(1024)
    except socket.timeout:
            sock.close()
            f.close()
            print("File Recieved! Recieved file saved as : recieved.txt in the directory")
            return addr

#function to send the sha256 of recievd file to the client.
def sendHash(addr,sha256):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as msg:
        print('Error in creating socket')
        print ('\nError Code : ' + str(msg[0]) + ' \nError Message: ' + msg[1])
        sys.exit()
    message =sha256
    data = message.encode('ascii')

    try :
        sock.sendto(data, addr)
    except socket.error as msg:
            print('Error in sending data')
            print('Error Code : ' + str(msg[0]) + ' Error Message ' + msg[1])
            sys.exit()
    sock.close()


#main
port = checkArgs()

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0',port))

except socket.error :
    print('Error in Binding the Port. Port either not avaiable or reserved. Please try with a different port no. >1024')
    sys.exit()

print ('Socket successfully binded')
print ('Listening on Port : ' + format(port))

addr = recieveFile()
sha256 = printSHA256('recieved')
sendHash(addr,sha256)
