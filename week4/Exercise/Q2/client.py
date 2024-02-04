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

def start_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (server_host, server_port)
    print("Do Ctrl+c to exit the program !!")

    try:
        while True:
            message = input("Type some text to send => ")
            client_socket.sendto(message.encode(), server_address)
            print(f"1. Client Sent : {message}")
            response, _ = client_socket.recvfrom(1024)
            print(f"2. Client received : {response.decode()}")
    except KeyboardInterrupt:
        print("\nClient is shutting down.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = calculatePort()
    start_client(SERVER_HOST, SERVER_PORT)
