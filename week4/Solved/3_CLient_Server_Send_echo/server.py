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
HOST = socket.gethostname()
PORT = calculatePort()
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print("Connection by ",addr)
		while True:
			data = conn.recv(1024)
			if data:
				print("Client:",data.decode())
				data = input("Enter message to a client")
			if not data:
				break
			conn.sendall(bytearray(data,'utf-8'))
	conn.close()