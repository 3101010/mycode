# -*- coding:utf-8 -*-
# date:2018-08-17 00:24
# p12

import socket
import threading

bind_ip = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)

#这是客户处理线程
def handle_client(client_socket):
    pass


while True:
    client, addr = server.accept()
    print ("[*] Accepted connection from: %s:%d" % addr)
    client.send("ACK!")




