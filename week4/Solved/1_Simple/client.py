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

host = socket.gethostname()
port=calculatePort()
s=socket.socket()
s.connect((host,port))
s.sendall(b'Welcome User!')
data = s.recv(1024)
s.close()
print(repr(data))