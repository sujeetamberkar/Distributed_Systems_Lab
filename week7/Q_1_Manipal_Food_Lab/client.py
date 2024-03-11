# Python3 program for a production line clock client at Manipal Foodie
from datetime import datetime
import threading
import socket
import time

def sendCurrentTime(production_line_client):
    while True:
        try:
            # Send current time to the master clock server
            current_time = str(datetime.now()).encode()
            production_line_client.send(current_time)
            print("Current time sent to master clock:", datetime.now())
            time.sleep(5)  # Wait for 5 seconds before sending the next update
        except Exception as e:
            print("Failed to send current time:", str(e))
            break

def receiveSynchronizedTime(production_line_client):
    while True:
        try:
            # Receive synchronized time from the master clock server
            synchronized_time_string = production_line_client.recv(1024).decode()
            if not synchronized_time_string:
                break  # Connection closed by the server
            synchronized_time = datetime.strptime(synchronized_time_string, '%Y-%m-%d %H:%M:%S.%f')
            print("Synchronized time received:", synchronized_time)
            # Here you would adjust the client clock to the synchronized time, if necessary
        except Exception as e:
            print("Failed to receive synchronized time:", str(e))
            break

def initiateProductionLineClock(port=8080):
    production_line_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Attempt to connect to the master clock server
    try:
        production_line_client.connect(('127.0.0.1', port))
        print("Connected to master clock server.")
    except Exception as e:
        print("Failed to connect to master clock server:", str(e))
        return

    # Start thread for sending current time to master clock
    send_time_thread = threading.Thread(target=sendCurrentTime, args=(production_line_client,))
    send_time_thread.start()

    # Start thread for receiving synchronized time from master clock
    receive_time_thread = threading.Thread(target=receiveSynchronizedTime, args=(production_line_client,))
    receive_time_thread.start()

if __name__ == '__main__':
    initiateProductionLineClock(port=8080)
