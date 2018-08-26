import socket
server_ip = '127.0.0.1'
server_port = 9090

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((server_ip, server_port))
print(s.recv(1024).decode('utf-8'))
for data in [b'zhaowei', b'zhaosan', b'lisi', b'zhangsi', b'zhaoqi', b'litang']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()