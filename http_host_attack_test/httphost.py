#! /usr/bin/python3
# -*- coding: utf-8 -*-
# #HTTP HOST头攻击漏洞验证
# #漏洞原理及危害：host头被恶意用户控制，https://www.cnblogs.com/ios9/p/7691540.html#_label1_0
# #使用方法 python3 httphost.py http://域名
# author:Net


from urllib import request
import urllib
import sys
import re
import chardet  # 增加编码自动识别
url=sys.argv[1]
header={'Host' : 'www.12315.com',
        'Connection' : 'keep-alive',
        'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Mobile Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8',
        }

try:
    req = request.Request(url, headers=header)
except Exception as e:
    print(e,'url错误！,请加http://')
else:
    try:
        req = request.Request(url, headers=header)
        u = request.urlopen(req)
        resp = u.read()
        char = chardet.detect(resp)['encoding']
        if re.match('.*www.12315.com', resp.decode(char)):
            print('存在漏洞')
        else:
            print('不存在漏洞')
    except urllib.error.HTTPError as e:
        if e.code >= 403:
            print(str(e.reason) + str(e.code) + ' ' + '漏洞可能不存在！')
    except urllib.error.URLError as e:
        print(str(e.reason)+ ' ' + '打不开，可域名和网络错误！')
    except Exception as e:
        print(e, '错误，漏洞可能不存在！')



#修复方法：
#在http.conf,或者vhosts.conf中（推荐）修改配置，禁止ip访问网站，指定网站域名。
#vhosts.conf 举例：

# NameVirtualHost *:80
#
# #首先拒绝所有通过ip访问网站,金盾加固,2017.12.29
# <VirtualHost *:80>
# 	ServerName 112.124.111.128
# 	<Location />
# 		Order allow,deny
# 		Deny from all
# 	</Location>
# </VirtualHost>
#
# #配置网站目录，并配置servername,金盾加固,2017.12.29
# <VirtualHost *:80>
# 	ServerName  www.sipo-hn.com.cn
# 	ServerAlias sipo-hn.com.cn sipo-hn.com sipo-hn.net www.sipo-hn.com.cn www.sipo-hn.com www.sipo-hn.net
# 	DocumentRoot "网站目录..."
# 	<Directory "网站目录...">
# 		Options  FollowSymLinks
# 		AllowOverride None
# 		Order allow,deny
# 		Allow from all
# 	</Directory>
# 	#后台地址限制--开始
# 	<location /jcms/>
# 		Order allow,deny
#
# 		# 南京大汉ip -10个
# 		Allow from 221.226.56.34 221.226.56.35 221.226.56.36 221.226.56.37 221.226.56.38 221.226.56.39 221.226.56.40 221.226.56.41 221.226.56.42 221.226.56.43
#
# 		# 金盾ip - 4个
# 		Allow from 117.158.3.66 219.150.168.226 218.28.142.106 222.143.24.148
#
# 		# 专利局ip - 12个
# 		Allow from 125.46.76.154 125.46.76.155 125.46.76.156 125.46.76.157 125.46.76.158 218.29.143.216 218.29.143.217 218.29.143.218 218.29.143.218 218.29.143.219 218.29.143.220 218.29.143.221 218.29.143.222 218.29.143.223
#
# 		#专利局ip - 北京临时
# 		#Allow from 219.142.19.58
# 	</location>
#
# 	<location /jcms/setup>
# 		Order allow,deny
# 	</location>
# 	#后台地址限制--结束
#
# </VirtualHost>
#


