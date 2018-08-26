# -*- coding:utf-8 -*-

from email.mime.text import MIMEText
import smtplib
from email.header import Header
from email.utils import parseaddr, formataddr


x = Header('来自SMTP的问候......abc', 'utf-8')
y = Header('zhaowei <15039671626@qq.com>', 'utf-8')
print (x)
print (y)
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
x = _format_addr('管理员 <%s>' % "463266963@qq.com")

print (x)


from_addr = '15039671626@139.com'
password = 'yd1503967'
to_addr = '463266963@qq.com'
smtp_server = 'smtp.139.com'


msg = MIMEText('hello,zhaowei!','plain','utf-8')
#msg['From'] = _format_addr('zhaowei<%s>' % from_addr)
msg['From'] = Header('python爱好者 <%s>' % from_addr, 'utf-8')
msg['to'] = _format_addr('管理员 <%s>' % "463266963@qq.com")
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
