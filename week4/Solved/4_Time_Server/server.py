import socket
import time
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

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = calculatePort()
serversocket.bind((host,port)) # Bind to the port
serversocket.listen(5) # Queue upto 5 request
while True:
	clientsocket,addr = serversocket.accept()
	print("Got a connection from %s ",str(addr))
	currentTime = time.ctime(time.time())+"\r\n"
	clientsocket.send(currentTime.encode('ascii'))
	clientsocket.close()