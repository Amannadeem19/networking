# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
# get ip of google
google_ip = socket.gethostbyname('www.google.com')

print(f"google ip : {google_ip}")
print(f"hostname: {hostname}" )
print(f"ip address: {ip_address}")

# get hostname using ip

host = socket.gethostbyaddr('8.8.8.8')
print(host)
host2 =socket.gethostbyaddr(ip_address)
print(f"hostname :{host2}")

# finding port and service name 

def find_service_name():
    
    protocolname='tcp'
    for port in [80,25]:
        print("Port :%s => Service name: %s" %(port, socket.getservbyport(port, protocolname)))

    print ("port %s => service name: %s" %(53, socket.getservbyport(53,'udp') ))
    
    

if __name__ == '__main__':
    find_service_name()