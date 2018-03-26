import json
import requests
import time
from bs4 import BeautifulSoup
import os

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
        'Referer': 'http://butian.360.cn/Reward/pub//Message/send',
        "Cookie":"__huid=11iG2Lxm6+ZYcs3gZYffTpfY3hSL9DFgEOVB2IVGdrCSY=; __guid=132730903.3081300459025730600.1511068627877.4731; __gid=156009789.597625749.1511068940809.1511069060148.3; __hsid=607590b042738ffc; Q=u%3D%25PQ%25S8%25O6%25R1%25PP%25RP%25PS%25P2%26n%3D%26le%3Drv53o2ScLzIcnzyhMl53WGDjZGLmYzAioD%3D%3D%26m%3D%26qid%3D108357034%26im%3D1_t0110241e46b6243004%26src%3D360chrome%26t%3D1; T=s%3Def372f4f334b11bd509f9be7171ef9db%26t%3D1511071681%26lm%3D%26lf%3D1%26sk%3Ddc28e065bfccfa0ef16cd0a4c95ef983%26mt%3D1511071681%26rc%3D%26v%3D2.0%26a%3D1; PHPSESSID=qucsabthphh4g2mt5am2020gi1; __q__=1511686950193; __DC_monitor_count=2; __DC_gid=156009789.597625749.1511068940809.1511686949655.5; __DC_sid=90162694.2805026889702643000.1511686924976.1587",
        'Connection': 'keep-alive'
    }
    for i in range(1,int(allPages)):
        data={
            's': '1',
            'p': i,
            'token': ''
        }
        time.sleep(3)
        res = requests.post('http://butian.360.cn/Reward/pub/Message/send', data=data,headers=headers,timeout=(4,20))
        allResult = {}
        allResult = json.loads(res.text)
        currentPage = str(allResult['data']['current'])
        currentNum = str(len(allResult['data']['list']))
        print('正在获取第' + currentPage + '页厂商数据')
        print('本页共有' + currentNum + '条厂商')
        for num in range(int(currentNum)):
            print('厂商名字:'+allResult['data']['list'][int(num)]['company_name']+'\t\t厂商类型:'+allResult\
                  ['data']['list'][int(num)]['industry']+'\t\t厂商ID:'+allResult['data']['list'][int(num)]['company_id'])
            base='http://butian.360.cn/Loo/submit?cid='
            with open('id.txt','a') as f:
                f.write(base+allResult['data']['list'][int(num)]['company_id']+'\n')
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
        'Cookie':'__huid=11iG2Lxm6+ZYcs3gZYffTpfY3hSL9DFgEOVB2IVGdrCSY=; __guid=132730903.3081300459025730600.1511068627877.4731; __gid=156009789.597625749.1511068940809.1511069060148.3; __hsid=607590b042738ffc; Q=u%3D%25PQ%25S8%25O6%25R1%25PP%25RP%25PS%25P2%26n%3D%26le%3Drv53o2ScLzIcnzyhMl53WGDjZGLmYzAioD%3D%3D%26m%3D%26qid%3D108357034%26im%3D1_t0110241e46b6243004%26src%3D360chrome%26t%3D1; T=s%3Def372f4f334b11bd509f9be7171ef9db%26t%3D1511071681%26lm%3D%26lf%3D1%26sk%3Ddc28e065bfccfa0ef16cd0a4c95ef983%26mt%3D1511071681%26rc%3D%26v%3D2.0%26a%3D1; PHPSESSID=10c71pkd4ueobg09pof2motvi6; __DC_monitor_count=4; __DC_gid=156009789.597625749.1511068940809.1511709137456.79; __DC_sid=138613664.3625595881020889000.1511707835325.7432; __q__=1511709138348',
        'Connection':'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control':'max-age=0'
    }
    with open('id.txt','r') as f:
        for target in f.readlines():
            target=target.strip()
            idnum=target.split("=")[1]
            getUrl=requests.get(target,headers=headers,timeout=(4,20))
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
    res = requests.post('http://butian.360.cn/Reward/pub/Message/send', data=data)
    allResult = {}
    allResult = json.loads(res.text)
    allPages = str(allResult['data']['count'])
    print('共' + allPages + '页')
    #spider()
    Url()