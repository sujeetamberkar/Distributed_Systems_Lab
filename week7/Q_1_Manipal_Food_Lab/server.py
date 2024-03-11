# Python3 program for the master clock at Manipal Foodie's testing lab
from datetime import datetime, timedelta
import threading
import socket

# Data structure to store information about each production line's clock
production_line_clocks = {}

def receiveClockTime(connector, address):
    while True:
        try:
            clock_time_string = connector.recv(1024).decode()
            if not clock_time_string:
                break  # Connection closed by the client
            clock_time = datetime.strptime(clock_time_string, '%Y-%m-%d %H:%M:%S.%f')
            clock_time_diff = datetime.now() - clock_time
            production_line_clocks[address] = {
                "clock_time": clock_time,
                "time_difference": clock_time_diff,
                "connector": connector
            }
            print("Clock data updated for production line:", address)
        except Exception as e:
            print("Error receiving time from", address, ":", str(e))
            break

def startConnecting(master_server):
    while True:
        connector, addr = master_server.accept()
        address = f"{addr[0]}:{addr[1]}"
        print(address, "connected successfully (Production Line)")
        current_thread = threading.Thread(target=receiveClockTime, args=(connector, address,))
        current_thread.start()

def getAverageClockDiff():
    time_difference_list = [clock["time_difference"] for clock in production_line_clocks.values()]
    if not time_difference_list:
        return timedelta(0)
    average_clock_difference = sum(time_difference_list, timedelta(0)) / len(time_difference_list)
    return average_clock_difference

def synchronizeAllClocks():
    while True:
        if production_line_clocks:
            average_clock_difference = getAverageClockDiff()
            synchronized_time = datetime.now() + average_clock_difference
            for address, clock in production_line_clocks.items():
                try:
                    clock['connector'].send(str(synchronized_time).encode())
                except Exception as e:
                    print("Error sending synchronized time to", address, ":", str(e))
        else:
            print("No production lines connected. Synchronization not applicable.")
        threading.Event().wait(5)  # Wait for 5 seconds before the next cycle

def initiateMasterClock(port=8080):
    master_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    master_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    master_server.bind(('', port))
    master_server.listen(10)
    print("Master Clock Server started on port", port)

    connecting_thread = threading.Thread(target=startConnecting, args=(master_server,))
    connecting_thread.start()

    sync_thread = threading.Thread(target=synchronizeAllClocks)
    sync_thread.start()

if __name__ == '__main__':
    initiateMasterClock(port=8080)
