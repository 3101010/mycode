# -*- coding:utf-8 -*-
#指定文本编码格式
#! /usr/bin/env python
#上面是为了在mac、linux上直接以./file.py运行程序。
# __author__="zhaowei"
import requests
import re
print('脚本关-第二题')
s = requests.Session()
url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
r = s.get(url).content.decode('utf-8')
# print(r)
match = re.findall(re.compile(r'(\d.*)=<'), r)[0]
print(match, '=', eval(match))
r = s.post(url, data = {"v": eval(match)}).content.decode('utf-8')
key = re.findall(re.compile(r'<body>.*is (.*?)\s*</body>'), r)[0]
print('key','=', key)