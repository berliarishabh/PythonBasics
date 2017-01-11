#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : file2-client.py
#date : 2016.10.17
#purpose : UDP client to send file, compute its sha256 and recive the hash from the server. Compare these two hash to get check whether the file has reached the server successfully
#if sha256 matches, file trf is successful, else it failed.
#version: 1.0.0
#features: Handles errors in user inputs and prompts the correct USAGE and error code.
#use of try except for better error handling.


import sys,socket,os,hashlib

#function to check if file exists?
def isFile (fileName) :
	if os.path.isfile(fileName):
		return 1

	else:
		return -1

#function to read file and send it through UDP socket.
#It also waits on the sha256 of the recieved file from the server and compares it with the hash of sent file.
#To validate file trf was Sucessful or not.
def sendFile(fileName, sha256):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as msg:
        print('Error in creating socket')
        print ('\nError Code : ' + str(msg[0]) + ' \nError Message: ' + msg[1])
        sys.exit()

    f = open(fileName, "rb")
    data = f.read(1024)
    while (data):
        try :
            sock.sendto(data, (serverIP,port))
            data = f.read(1024)
        except socket.error as msg:
                print('Error in sending data')
                print('Error Code : ' + str(msg[0]) + ' Error Message ' + msg[1])
                sys.exit()

    data,addr = sock.recvfrom(1024)
    recieved_sha256 = data.decode('ascii')
    if(sha256 == recieved_sha256):
        print('SHA256 Valid! File Transfer Sucessful')
    else :
        print('SHA256 Invalid! File Transfer Failed. Try again.')
    sock.close()
    f.close()

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

	if (len(sys.argv) != 4):
		print("\nERROR! Please specify the 'Server IP' as argument1, 'Port' as argument2, 'Filename' as argument3\nUSAGE: " + sys.argv[0] + " 127.0.0.1 [>1024] filename.ext\n"   )
		sys.exit()
	return sys.argv[1],int(sys.argv[2]),sys.argv[3]


#main
serverIP, port, fileName = checkArgs()

if(isFile(fileName) == -1):
	print ("ERROR! File not found!")

else:
    sha256 = printSHA256(fileName)

    sendFile(fileName, sha256)


quit()
