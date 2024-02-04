import socket
import os
from _thread import *

def calculatePort():
	while True: 
		l=int(input('Enter Lower Limit :  \n'))
		if l>5 :
			break
	while True:
		u=int(input('Enter Upper Limit : \n'))
		if u>25:
			break
	r=1000*(u-l)+l
	return r

def threaded_client(connection, thread_count):
    connection.send(str.encode('Welcome to the Server'))
    while True:
        data = connection.recv(2048)
        if not data:
            print('Client Disconnected')
            break
        print('Received from client ' + str(thread_count) + ': ' + data.decode())
        connection.sendall(str.encode('Server response: ' + data.decode()))
    connection.close()

ServerSocket = socket.socket()
host = ''
port = calculatePort()

ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Waiting for a Connection..')
ServerSocket.listen(5)

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ThreadCount))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()