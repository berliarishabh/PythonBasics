#!/usr/bin/env python3

#author : Rishabh Berlia rishabh.berlia@colorado.edu
#name : file1-server.py
#date : 2016.10.17
#purpose : Simple UDP server to recieve messages from client
#version: 1.0.0
#features: Handles errors in user inputs like wrong port specified or port already in use, prompts the correct USAGE and error code.
#use of try except for better error handling. Also handles KeyBoard interrupt and Exceptions avoiding traceback.

import sys,socket


#function to check if argument is passed or not.
def checkArgs():

	if (len(sys.argv) != 2):
		print("\nERROR! Please specify the 'Port' as argument1 \nUSAGE: " + sys.argv[0] + " [>1024]\n"   )
		sys.exit()
	return int(sys.argv[1])


#main
def main():
    try:
        port = checkArgs()

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(('0.0.0.0',port))

        except socket.error :
            print('Error in Binding the Port. Port either not avaiable or reserved. Please try with a different port no. >1024')
            sys.exit()

        print ('Socket successfully binded')
        print ('Listening on Port : ' + format(port))

        #listen on the port for messages from UP client

        while 1:

            data,addr = sock.recvfrom(65538)
            text = data.decode('ascii')
            print('The client has sent the following message: ' + '\'' + text + '\'' '\nfrom IP : ' + format(addr[0]) + ' and ephemeral port : ' + format(addr[1]))

        sock.close()

    except KeyboardInterrupt:
        print ("Shutdown requested...exiting")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

main()
