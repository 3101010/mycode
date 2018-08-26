import socket
import threading
import time

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9090))

print('Bind UDP on 9090...')
while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    time.sleep(1)
    s.sendto(b'Hello, %s!' % data, addr)

