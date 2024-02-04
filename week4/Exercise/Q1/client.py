import socket

# Define the server's IP address and port you want to connect to
server_ip = '127.0.0.1'
server_port = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send a message to the server
message = b'What is the current time and day?'
client_socket.sendto(message, (server_ip, server_port))

# Receive the response from the server and close the socket
response, _ = client_socket.recvfrom(4096)
print(f"Server response: {response.decode()}")

client_socket.close()
