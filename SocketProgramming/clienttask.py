# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 11:57:37 2023

@author: StudentUser
"""

import socket

while True:
    
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # connnecting to the server address
    s.connect(('192.168.56.1', 1234))
    
    try:
        # send messages
        messages = input('enter a message: ')
        s.sendall(messages.encode())
        
        # 1024 shows max number of bytes that can be send
        receive_data=s.recv(1024)
        print(f"Receive data : {receive_data.decode()}")
    
    finally:
        # clean the socket
        s.close()
    




