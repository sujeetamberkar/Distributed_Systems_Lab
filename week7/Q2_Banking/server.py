import socket
from datetime import datetime

def initiateTimeServer(port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', port))
        s.listen()
        print(f"Time Server running on port {port}...")
        
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                # Sending current server time to the client
                current_time = str(datetime.now()).encode()
                conn.sendall(current_time)

if __name__ == '__main__':
    initiateTimeServer(port=8080)
