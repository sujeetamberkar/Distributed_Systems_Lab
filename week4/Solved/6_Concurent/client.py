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



ClientSocket = socket.socket()
host = socket.gethostname()
port = calculatePort()

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode())

while True:
    Input = input('Client Say Something: ')
    ClientSocket.send(str.encode(Input))
    if Input.lower() == 'exit':
        break
    Response = ClientSocket.recv(1024)
    print('From Server : ' + Response.decode())

ClientSocket.close()
