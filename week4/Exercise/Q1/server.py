import socket
import datetime

# Define the server's IP address and port
server_ip = '127.0.0.1'  # localhost
server_port = 12345

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server's IP address and port
server_socket.bind((server_ip, server_port))

print("UDP Time Server is up and running.")

while True:
    # Wait for a client to send a message
    message, client_address = server_socket.recvfrom(1024)
    
    # Get the current time and day
    now = datetime.datetime.now()
    current_time_day = now.strftime("%Y-%m-%d %H:%M:%S, %A")
    
    # Send the current time and day back to the client
    server_socket.sendto(current_time_day.encode(), client_address)
