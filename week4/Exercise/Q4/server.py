import socket

serverIP = 'localhost'
serverPort = 16000
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind((serverIP, serverPort))
serverSock.listen(1)
print("TCP server has started and is ready to receive")

while True:
    connection, addr = serverSock.accept()
    
    # Accumulate data if split across packets
    data = b""
    while True:
        part = connection.recv(1024)
        data += part
        if len(part) < 1024:
            break

    if not data:
        break

    # Decode the received bytes object back into a string
    temp = [float(x) for x in data.decode().split(' ')]

    print("Received data:", temp)
    length = len(temp)
    maximum = max(temp)
    minimum = min(temp)
    total = sum(temp)
    mean = total / length
    
    msg = str(total) + " " + str(minimum) + " " + str(maximum) + " " + str(mean)
    
    # Send encoded string as bytes
    connection.send(msg.encode())

    connection.close()  # Close the connection after sending the data
