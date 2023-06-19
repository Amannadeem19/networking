import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 9999)

# Data to be sent
name = 'John'
place = 'New York'
age = '30'
country = 'USA'
data = ','.join([name, place, age, country])

# Send the data to the server
sock.sendto(data.encode(), server_address)

# Receive a response from the server
response, server = sock.recvfrom(4096)
print(response.decode())
