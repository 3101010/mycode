import json
import requests
import time
from bs4 import BeautifulSoup
import os
import pymysql
import sqlite3

# #mysql
# db = pymysql.connect("localhost","root","1q2w!Q@W","butian")
# cursor = db.cursor()

#sqlite
db1 = sqlite3.connect('butian.db')
cursor1 =   db1.cursor()



def spider():
    '''
    爬取所有公益厂商的ID
    保存为id.txt
    :return:
    '''
    headers = {
        'Host': 'butian.360.cn',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie':'__guid=132730903.4440770603871268400.1520390803017.5654; __huid=11CubMWdflqvoDYXEj8aSfRALh4waGg2TUdpM8EHYDXqY=; UM_distinctid=161fef3bf101cf-067004411e4e7a-1e5a2d42-100200-161fef3bf12126; Qs_lvt_168574=1526269048; Qs_pv_168574=4190023083885861000; _ga=GA1.2.382577052.1526614019; __gid=133660893.509053621.1520837988924.1535087918014.69; __hsid=cfc044660d41bca8; Q=u%3D360H996161374%26n%3D%26le%3DAQLmZwL2BGLmWGDjpKRhL29g%26m%3D%26qid%3D996161374%26im%3D1_t0130249639129f6be7%26src%3D360chrome%26t%3D1; T=s%3De8834ed1d029776112932035410d9685%26t%3D1533952248%26lm%3D%26lf%3D1%26sk%3D790348a59b880faa8b65defdbd1fe966%26mt%3D1533952248%26rc%3D%26v%3D2.0%26a%3D1; PHPSESSID=e4n8fis9k255o3a8o7d8rgc5o2; __DC_monitor_count=2; __DC_gid=133660893.509053621.1520837988924.1535251894827.479; __DC_sid=90162694.1582259957482741200.1535251894822.198; test_cookie_enable=null; __q__=1535251895346',
        'Referer': 'http://butian.360.cn/Reward/pub//Message/send',
        'Connection': 'keep-alive'
    }
    for i in range(1,int(allPages)):
        data={
            's': '1',
            'p': i,
            'token': ''
        }
        # time.sleep(3)
        session = requests.session()
        res = session.post('http://butian.360.cn/Reward/pub/Message/send', data=data,headers=headers,timeout=(4,20))
        allResult = {}
        allResult = json.loads(res.text)
        currentPage = str(allResult['data']['current'])
        currentNum = str(len(allResult['data']['list']))
        print('正在获取第' + currentPage + '页厂商数据')
        print('本页共有' + currentNum + '条厂商')
        for num in range(int(currentNum)):
            # print('厂商名字:'+allResult['data']['list'][int(num)]['company_name']+'\t\t厂商类型:'+allResult\
            #       ['data']['list'][int(num)]['industry']+'\t\t厂商ID:'+allResult['data']['list'][int(num)]['company_id'])
            # base='http://butian.360.cn/Loo/submit?cid='
            # with open('id.txt','a') as f:
            #     f.write(base+allResult['data']['list'][int(num)]['company_id']+'\n')
            sql = "replace into butian(company_id, company_name, industry, company_url) VALUES ('%s' , '%s', '%s', null)" % (allResult['data']['list'][int(num)]['company_id'], allResult['data']['list'][int(num)]['company_name'], allResult['data']['list'][int(num)]['industry'])
            print ("sql" + sql)
            cursor1.execute(sql)
            db1.commit()
    db1.close()

#sqlite
db2 = sqlite3.connect('butian.db')
cursor2 =  db2.cursor()
def Url():
    '''
    遍历所有的ID
    取得对应的域名
    保存为target.txt
    :return:
    '''
    headers={
        'Host':'butian.360.cn',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Referer':'http://butian.360.cn/Reward/pub',
        'Cookie':'__guid=132730903.4440770603871268400.1520390803017.5654; __huid=11CubMWdflqvoDYXEj8aSfRALh4waGg2TUdpM8EHYDXqY=; UM_distinctid=161fef3bf101cf-067004411e4e7a-1e5a2d42-100200-161fef3bf12126; Qs_lvt_168574=1526269048; Qs_pv_168574=4190023083885861000; _ga=GA1.2.382577052.1526614019; __gid=133660893.509053621.1520837988924.1535087918014.69; __hsid=cfc044660d41bca8; Q=u%3D360H996161374%26n%3D%26le%3DAQLmZwL2BGLmWGDjpKRhL29g%26m%3D%26qid%3D996161374%26im%3D1_t0130249639129f6be7%26src%3D360chrome%26t%3D1; T=s%3De8834ed1d029776112932035410d9685%26t%3D1533952248%26lm%3D%26lf%3D1%26sk%3D790348a59b880faa8b65defdbd1fe966%26mt%3D1533952248%26rc%3D%26v%3D2.0%26a%3D1; PHPSESSID=e4n8fis9k255o3a8o7d8rgc5o2; __DC_monitor_count=2; __DC_gid=133660893.509053621.1520837988924.1535251894827.479; __DC_sid=90162694.1582259957482741200.1535251894822.198; test_cookie_enable=null; __q__=1535251895346',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control':'max-age=0'
    }
    # session = requests.session()
    # cursor2.execute("select company_id from butian;")

    with open('id.txt','r') as f:
        for target in f.readlines():
            target=target.strip()
            idnum=target.split("=")[1]
            getUrl=session.get(target,headers=headers,timeout=(4,20))
            print ("HTTP/1.1 %s" % getUrl.status_code)
            result=getUrl.text
            info=BeautifulSoup(result,'html.parser')
            url=info.find(name='input',attrs={"name":"host"})
            name = info.find(name='input', attrs={"name": "company_name"})
            lastUrl=url.attrs['value']
            print('厂商:' + name.attrs['value'] + '\t网址:' + url.attrs['value'] + '\t厂商ID号:'+ idnum)
            with open('target.txt','a') as t:
                t.write(lastUrl+'\n')
            time.sleep(3)
    print('The target is right!')
if __name__=='__main__':
    print (os.getcwd())
    data = {
            's': '1',
            'p': '1',
            'token': ''
        }
    session = requests.session()
    res = session.post('http://butian.360.cn/Reward/pub/Message/send', data=data)
    allResult = {}
    allResult = json.loads(res.text)
    allPages = str(allResult['data']['count'])
    print('共' + allPages + '页')
    spider()
    #Url()