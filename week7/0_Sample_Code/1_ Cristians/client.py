import socket
import datetime
from dateutil import parser
from timeit import default_timer as timer

# Function used to Synchronize client process time
def synchronizeTime():
    s = socket.socket()
    # Server port
    port = 8011
    # Connect to the clock server on local computer
    s.connect(('127.0.0.1', port))
    request_time = timer()
    # Receive data from the server
    server_time = parser.parse(s.recv(1024).decode())
    response_time = timer()
    actual_time = datetime.datetime.now()
    print("Time returned by server: " + str(server_time))
    process_delay_latency = response_time - request_time
    print("Process Delay latency: " + str(process_delay_latency) + " seconds")
    print("Actual clock time at client side: " + str(actual_time))
    # Synchronize process client clock time using Cristian's formula
    client_time = server_time + datetime.timedelta(seconds=(process_delay_latency) / 2)
    print("Synchronized process client time: " + str(client_time))
    # Calculate synchronization error
    error = actual_time - client_time
    print("Synchronization error: " + str(error.total_seconds()) + " seconds")
    s.close()

# Driver function
if __name__ == '__main__':
    # Synchronize time using clock server
    synchronizeTime()
