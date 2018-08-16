# -*- coding:utf-8 -*-
# date:2018-08-17 00:24
# p11 server

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))

print ("Bind UDP on 9999...")
while True:
    data, addr = s.recvfrom(4096)
    print('Received from %s:%s.' % addr)
    s.sendto("Hello, %s" % data, addr)






