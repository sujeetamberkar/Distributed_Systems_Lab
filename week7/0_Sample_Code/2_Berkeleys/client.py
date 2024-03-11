# Python3 program imitating a client process
from datetime import datetime
import threading
import socket
import time

def sendTime(slave_client):
    while True:
        try:
            # Send current time to the server
            slave_client.send(str(datetime.now()).encode())
            print("Recent time sent successfully")
            time.sleep(5)  # Wait for 5 seconds before sending the next time
        except Exception as e:
            print("Error sending time:", str(e))
            break

def receiveTime(slave_client):
    while True:
        try:
            # Receive synchronized time from the server
            synchronized_time_string = slave_client.recv(1024).decode()
            if not synchronized_time_string:
                break  # Connection closed by the server
            synchronized_time = datetime.strptime(synchronized_time_string, '%Y-%m-%d %H:%M:%S.%f')
            print("Synchronized time at the client is:", synchronized_time)
        except Exception as e:
            print("Error receiving synchronized time:", str(e))
            break

def initiateSlaveClient(port=8080):
    slave_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    slave_client.connect(('127.0.0.1', port))

    send_thread = threading.Thread(target=sendTime, args=(slave_client,))
    send_thread.start()

    receive_thread = threading.Thread(target=receiveTime, args=(slave_client,))
    receive_thread.start()

if __name__ == '__main__':
    initiateSlaveClient(port=8080)
