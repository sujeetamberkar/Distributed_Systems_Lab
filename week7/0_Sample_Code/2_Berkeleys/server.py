# Python3 program imitating a clock server
from datetime import datetime, timedelta
import threading
import socket

# Data structure used to store client address and clock data
client_data = {}

def receiveClockTime(connector, address):
    while True:
        try:
            # Receive clock time
            clock_time_string = connector.recv(1024).decode()
            if not clock_time_string:
                break  # Connection closed by the client
            clock_time = datetime.strptime(clock_time_string, '%Y-%m-%d %H:%M:%S.%f')
            clock_time_diff = datetime.now() - clock_time
            client_data[address] = {
                "clock_time": clock_time,
                "time_difference": clock_time_diff,
                "connector": connector
            }
            print("Client Data updated with:", address)
        except Exception as e:
            print("Error receiving time from", address, ":", str(e))
            break

def startConnecting(master_server):
    while True:
        # Accepting a client / slave clock client
        connector, addr = master_server.accept()
        slave_address = str(addr[0]) + ":" + str(addr[1])
        print(slave_address, "got connected successfully")
        current_thread = threading.Thread(target=receiveClockTime, args=(connector, slave_address,))
        current_thread.start()

def getAverageClockDiff():
    time_difference_list = [client["time_difference"] for client in client_data.values()]
    if not time_difference_list:
        return timedelta(0)
    average_clock_difference = sum(time_difference_list, timedelta(0)) / len(time_difference_list)
    return average_clock_difference

def synchronizeAllClocks():
    while True:
        if client_data:
            average_clock_difference = getAverageClockDiff()
            synchronized_time = datetime.now() + average_clock_difference
            for client_addr, client in client_data.items():
                try:
                    client['connector'].send(str(synchronized_time).encode())
                except Exception as e:
                    print("Error sending synchronized time to", client_addr, ":", str(e))
        else:
            print("No clients connected. Synchronization not applicable.")
        threading.Event().wait(5)  # Wait for 5 seconds before the next cycle

def initiateClockServer(port=8080):
    master_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    master_server.bind(('', port))
    master_server.listen(10)
    print("Clock server started on port", port)

    connecting_thread = threading.Thread(target=startConnecting, args=(master_server,))
    connecting_thread.start()

    sync_thread = threading.Thread(target=synchronizeAllClocks)
    sync_thread.start()

if __name__ == '__main__':
    initiateClockServer(port=8080)
