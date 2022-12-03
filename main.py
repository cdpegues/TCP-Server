#!/usr/bin/python3

#https://www.youtube.com/watch?v=xbeNk-UQ0kE
#creds to HackerSploit for tutorial. 

#imports
import socket

#define serversocket variable. Specify AF_INET for IPv4 over SOCK_STREAM or TCP.
#this creates the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host is the server IP addr
host = socket.gethostname()

port = 4444

#binds host and port variable to socket
serversocket.bind((host, port))

#set up a TCP listener for one connection
serversocket.listen(1)

#while all of the above is true, establish the connection to the clientsocket
while True:

    #accepts TCP information from client
    clientsocket, address = serversocket.accept()
    
    #connection banner for the server
    print("Connection Successful from" % str(address))
    
    #connection banner for the client
    message = 'Thank you for connecting to the server' + '\r\n'

    #actualy sends the message to the client after successful connection
    clientsocket.send(message)
    
    #closes the client socket while any of this information is true
    clientsocket.close()
