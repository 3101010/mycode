import socket

target_host = "wiki.viewcn.cn"
target_port = 80

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((target_host, target_port))

s.send(b'GET / HTTP/1.1\r\nHost: wiki.viewcn.cn\r\nConnection: Close\r\n\r\n')

#res = s.recv(4096)
buffer = []

while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()

print(data)

header, html = data.split(b'\r\n\r\n',1)

with open('viewcn.html', 'wb') as f:
    f.write(html)

