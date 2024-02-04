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
port = calculatePort()
s = socket.socket()
s.bind((host,port))
s.listen(5)
conn,addr = s.accept()
print("Got connection from ",addr[0],'(',addr[1],")")
print("Thank You for connection")
while True:
	data = conn.recv(1024)
	if not data:
		break
	conn.sendall(data)
conn.close()
	