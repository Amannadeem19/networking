import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific IP address and port
server_address = ('localhost', 9999)
sock.bind(server_address)

while True:
    print('Waiting for data...')
    # Receive data from the client
    data, client_address = sock.recvfrom(4096)
    print('Received {} bytes from {}'.format(len(data), client_address))

    # Decode the data to extract the name, place, age, and country
    name, place, age, country = data.decode().split(',')

    # Print the received data
    print('Name: {}\nPlace: {}\nAge: {}\nCountry: {}\n'.format(name, place, age, country))

    # Send a response to the client
    message = 'Data received successfully'
    sock.sendto(message.encode(), client_address)
