# import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# name = input('please input your name：')
# while True:
#     data = input('please input your messages：')
#     s.sendto(bytes(name + ':' + data,encoding='utf-8'), ('127.0.0.1', 9090))
#     print (s.recv(1024).decode('utf-8'))
# s.close()

import socket
import threading,time
import re

def udpLink(sock,addr):
    while True:
        time.sleep(0.1)
        print(sock.recv(1024).decode('utf-8'))

print('input your sever ip:')
while True:
    ip = input()
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",ip):
        break
    print('unlawful IP')
print('input your name:')
name = input()
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto(bytes(name+':'+'online',encoding = 'utf-8'),(ip,9999))
t = threading.Thread(target = udpLink,args=(s,(ip,9999)))
t.start()
while True:
    data = input()
    s.sendto(bytes(name+':'+data,encoding = 'utf-8'),(ip,9999))
s.close()