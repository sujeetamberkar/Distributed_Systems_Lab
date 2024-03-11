import socket
from datetime import datetime

def synchronizeTimeWithServer(server_ip='127.0.0.1', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        server_time = s.recv(1024).decode()
        print(f"Synchronized Time from Server: {server_time}")
        # Simulate setting this time as the client's current time
        client_time = datetime.now()
        print(f"Client's Original Time (before synchronization): {client_time}")
        client_time = server_time  # Assuming direct assignment for demonstration
        print(f"Client's New Time (after synchronization): {client_time}")

if __name__ == '__main__':
    synchronizeTimeWithServer(port=8080)
