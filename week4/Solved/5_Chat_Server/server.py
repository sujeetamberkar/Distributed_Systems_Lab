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
s.bind((HOST,PORT))
s.listen()
print("\n Waiting for incomming connection")
conn,addr = s.accept()
print("Recieved connection from ",addr[0], "(",addr[1],")\n")
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name,"has connected to the chat room\nEnter [e] to exit chat room\n")
name = input(str("Enter your name:\t"))
conn.send(name.encode())
while True:
	message = input (str("Me:\t"))
	if message == 'e':
		message = "Left the chat room!"
		conn.send(message.encode())
		print("\n")
		break
	conn.send(message.encode())
	message=conn.recv(1024)
	message = message.decode()
	print(s_name,":",message)
s.close()