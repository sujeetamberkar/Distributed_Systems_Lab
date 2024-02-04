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
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # UDP
udp_host = socket.gethostname()
udp_port = calculatePort()

msg = "UDP Program"
print("UDP target IP: ",udp_host)
print("UDP target Port",udp_port)
sock.sendto(msg.encode(),(udp_host,udp_port))