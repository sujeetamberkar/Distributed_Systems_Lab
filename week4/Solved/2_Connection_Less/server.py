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
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP
udp_host = socket.gethostname()
udp_port = calculatePort()
sock.bind((udp_host,udp_port))

while True:
	print("Waiting for client")
	data,addr = sock.recvfrom(1024)
	print("Recieved message:",data.decode(),"from",addr)
	