# encoding=utf-8

import paramiko
import time

client = paramiko.SSHClient()
client.load_system_host_keys()

# connect to client
client.connect('10.8.4.68', 22, 'admin', 'admin', allow_agent=False, look_for_keys=False)

# get shell
ssh_shell = client.invoke_shell()

# ready when line endswith '>' or other character
while True:
    line = ssh_shell.recv(1024)
    # print line
    if line and line.endswith('>'):
        break;

# send command
ssh_shell.sendall('display arp' + '\n')

# get result lines
lines = []
while True:
    line = ssh_shell.recv(1024)
    if line and line.endswith('>'):
        break;
    lines.append(line)
result = ''.join(lines)

# print result
print(result)


































# paramiko
# SSH
# 模块简单应用。
# 目的：需要ssh链接到Linux主机，执行telnet
# 命令，抓回显匹配制定内容。

# ssh - -->执行telnet到本地端口 - -->执行类似
# ls
# 的命令。匹配命令执行后的特定回显字段。

# 官方文档地址：http: // docs.paramiko.org / en / 2.0 / api / client.html

# 准备：pip
# install
# paramiko
# 模块。

# import paramiko

# ssh = paramiko.SSHClient()  # 创建sshclient
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 目的是接受不在本地Known_host文件下的主机。
# ssh.connect(ip, port, username, passwd)  # connect 函数可以接受很多参数，本例只列举4个主要的其他参数请见文档。

# # stdin,stdout,stderr = ssh.exec_command(cmd,bufsize,timeout) #exec_command参数使用只需要执行一次的命令，因为执行完该命令以后，shell会自动回到ssh初始连接的shell状态下，（表达不好，可以看官方文档。），stdin，out,err,对应shell下的标准输入，输出和错误。

# # stdin.write('y'+'\n') #这样通过标准输入输入命令

# # print stdout.read() #输出标准输出。

# # exec_command(command, bufsize=-1, timeout=None, get_pty=False)

# # Execute a command on the SSH server. A new Channel is opened and the requested command is executed. The command’s input and output streams are returned as Python file-like objects representing stdin, stdout, and stderr.在SSH server上执行命令，打开新的channel并执行命令，该命令返回的input，output数据流都是file-like对象。可以使用read，readline，readlines方法来将file-like数据变成string类型。

# chan = ssh.invoke_shell()  # 在SSH server端创建一个交互式的shell，且可以按自己的需求配置伪终端，可以在invoke_shell()函数中添加参数配置。

# chan.send(cmd + '\n')  # 利用send函数发送cmd到SSH server，添加'\n'做回车来执行shell命令。注意不同的情况，如果执行完telnet命令后，telnet的换行符是\r\n

# chan.recv(bufsize)  # 通过recv函数获取回显。

# 这样基本的函数与方法已经具备了，需要如何定制，就自己写个函数就可以了。