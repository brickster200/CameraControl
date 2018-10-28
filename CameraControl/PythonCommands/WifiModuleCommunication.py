#!/usr/local/bin/python3
#send data to IP address out of laptop port probably just array of servo arguments if that possible
#socket oibrary might be the way, and need to create a gui to go with it
# esp8266 can be used as stand alone board with right firmware but think it can be used as an add on to arduino uno
# http server client way of sending the dta through a website thingy

import socket
import time
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #opens new socket

packet = random._urandom(1024)

ip = '127.0.0.7'
port = 8000
duration = 1
timeout = time.time() + float(duration)
sent = 0
print('running')
while True:
    if time.time() > timeout:
        print(sent, 'breaking')
        break
    else:
        pass
    sock.sendto(packet, (ip, port))
    sent = sent + 1
    print('packet %s sent to %s at %s'%(sent, ip, time.time()))

