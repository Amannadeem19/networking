# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 11:57:49 2023

@author: StudentUser
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket created')

# Binding the specific address and port 
s.bind(('192.168.56.1', 1234))

# listen for incoming connnections

s.listen(2) 


while True:
    # returns the object of client connection for send and receiving data
    # address of the client which is ip + port
    print("Waiting for connection ...")
    
    connection,client_addr = s.accept()
    
    # print("connected with ", client_addr)
    
    # send and receive msgs
    try:
        
        
        data = connection.recv(1024)
            
        print(f"message received from client: {data.decode()}" )
            
        message = input('enter message for client: ')
        
        connection.sendall(message.encode())
        
    
    finally:
        connection.close()
        
s.close()
    