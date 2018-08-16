# -*- coding:utf-8 -*-
# date:2018-08-17 00:24
# p10

import socket

target_host = "127.0.0.1"
target_port = 9999

#建立一个socket对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#连接服务端
client.connect((target_host, target_port))

client.send("GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n")

response = client.recv(4096)

print(response)


