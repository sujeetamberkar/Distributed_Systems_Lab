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

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print("Do Ctrl+c to exit the program !!")
    print("####### Server is listening #######")

    try:
        while True:
            message, client_address = server_socket.recvfrom(1024)
            print(f"2. Server received: {message.decode()}")
            response = input("Type some text to send => ")
            server_socket.sendto(response.encode(), client_address)
            print(f"1. Server sent : {response}")
            print("####### Server is listening #######")
    except KeyboardInterrupt:
        print("\nServer is shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = calculatePort()
    start_server(HOST, PORT)
