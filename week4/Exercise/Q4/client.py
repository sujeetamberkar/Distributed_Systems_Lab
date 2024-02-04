import socket

serverIP = 'localhost'
serverPort = 16000
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((serverIP, serverPort))

# Use input instead of raw_input for Python 3
message = input("Input integers with space in between: ")
message2 = input("Enter the length of the set: ")

# In Python 3, strings need to be encoded before being sent over the network
clientSock.send(message.encode())
clientSock.send(message2.encode())

data = clientSock.recv(1024)

# Decode the received bytes object back into a string
temp = [float(x) for x in data.decode().split(' ')]

print("The total of all numbers is: " + str(temp[0]))
print("The lowest number is: " + str(temp[1]))
print("The highest number is: " + str(temp[2]))
print("The mean is: " + str(temp[3]))

clientSock.close()
