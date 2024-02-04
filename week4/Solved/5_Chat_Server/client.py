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
s = socket.socket()
name = input(str('\n Enter your name:\n'))
print("Trying to connect to ",HOST,"(",PORT,")")
s.connect((HOST, PORT))
print("Connected")
s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name," has joined the chat room\n Enter e to exit the chat room\n")
while True:
	message = s.recv(1024)
	message = message.decode()
	print(s_name,":",message)
	message = input (str("Me:"))
	if message == "e":
		message = "Left chat room"
		s.send(message.encode())
		print("\n")
		break
	s.send(message.encode())

s.close()