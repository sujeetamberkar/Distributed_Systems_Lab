import socket
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
HOST = socket.gethostname() #The server's hostname or IP address
PORT = calculatePort()

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	s.sendall(b"Hello World")
	data = s.recv(1024)
	print("Recieved Connection")
	print("Server:", data.decode())
	