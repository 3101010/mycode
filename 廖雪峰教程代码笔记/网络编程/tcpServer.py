import socket
import threading
import time

server_ip = '127.0.0.1'
server_port = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server_ip, server_port))
s.listen(5)
print('Wating for connetction.......')

def tcpLink(sock, addr):
    print('Accept new connection from %s:%s..' % addr)
    sock.send(b'Webcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock, addr = s.accept()
    #addr 是一个元组包含了地址和端口
    # sock是套接字对象：<socket.socket fd=276, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9090), raddr=('127.0.0.1', 15347)>
    t = threading.Thread(target=tcpLink, args=(sock, addr))
    t.start()

