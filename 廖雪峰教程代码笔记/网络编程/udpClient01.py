import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'zhaowei',b'zhangsan',b'lisi']:
    s.sendto(data,('127.0.0.1', 9090))
    print (s.recv(1024).decode('utf-8'))
s.close()