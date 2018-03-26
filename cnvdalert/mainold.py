#!/usr/bin/env python
#encoding:utf-8
#-*- coding:utf-8 -*-
"""
@author:Liod
@file:main.py
@time:18-1-19上午11:47
"""

import requests,re,datetime,smtplib,time,sys
from lxml import etree
from email.mime.text import MIMEText
from email.header import Header
from setting import *
from selenium import webdriver
import logging
# from collections import Counter

class BugSpider(object):

    def __init__(self):
        self.bugUrl = "http://www.cnvd.org.cn/webinfo/list?type=14"
        self.requests = requests.session()
        self.mail = ["222.143.21.161", "xxzxaqyw", "xxzx0714"]
        self.responseContent = ""


    def spiderBaner(self):
        headers = {
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0",
	        "Referer":"http://www.cnvd.org.cn/",
            "Accept-Language":"zh-CN,zh;q=0.9",
            "Cookie":self.getCookie(),
            "Host":"www.cnvd.org.cn",
        }

        return headers


    def getUrlResponse_Result(self):
        responseResult = {}
        response = self.requests.get(self.bugUrl, headers = self.spiderBaner())
        date = re.findall(r'<td width="13%">(.*?)</td>' , response.content)
        current_click = re.findall(r'<td width="9%">(.*?)</td>', response.content)
        pageTree = etree.HTML(response.content)
        href = map(lambda x:self.bugUrl.split("/")[0] + "//" + self.bugUrl.split("/")[2] + x, pageTree.xpath('//tr/td/a/@href'))
        title = map(lambda x:x.strip(), pageTree.xpath('//tr/td/a/text()'))
        for i in range(0, len(title)):
            responseResult["%s" % (date[i])] = [title[i], href[i], date[i], current_click[i]]
        self.responseContent = responseResult
        return responseResult


    def getDateUpdate(self, dateResult):
        dateRes = filter(lambda x:x, dateResult)
        #yestday = datetime.date.today() - datetime.timedelta(days=15)
        yestday = datetime.date.today()
        yestdayTime = yestday.strftime("%Y-%m-%d")
        nowTime = datetime.datetime.now().strftime("%Y-%m-%d")
        # return filter(lambda x:x==nowTime, dateResult)
        updateDate = filter(lambda x: x >= yestdayTime, dateRes)
        return map(lambda x: dateResult[x], updateDate)

        #return filter(lambda x:x==nowTime, dateResult)

    def modileText(self, code=-1):
        if code == -1:
            result = ""
            modileText = self.getDateUpdate(self.responseContent)
            for i in modileText:
                # print i
                result += u"漏洞标题:%-39s\n详细信息:%-45s\n漏洞预警时间:%-10s \n漏洞点击量:%s \n\n\n" % (i[0], i[1], i[2], i[3])
            ress = """%s""" % result.encode("utf-8")
            return ress
        else:
            return """暂时未监测到新的漏洞信息！"""

    def sendMail(self, receiveMailName=[], receiveAuthor="" , code=-1):
        nowTime = datetime.datetime.now().strftime("%Y-%m-%d")
        message = MIMEText('%s\n%s\n%s'%('信息安全漏洞预警:', self.modileText(code), '******本预警邮件由金盾信安预警系统自动发送，如需退订请回复本邮件******@测试版'), 'plain', 'utf-8')
        message['From'] = "信息安全预警 <%s>" % "hngsteam@icsp.org.cn"
        message['To'] = ",".join(receiveAuthor)
        if receiveAuthor == adminList(): 
            subject = "%s 管理员你好！今天未发现新的漏洞预警！" % nowTime
        else:
            subject = "%s 金盾信安提醒您！您收到一个新的信息安全漏洞预警！" % nowTime
        message['Subject'] = Header(subject, 'utf-8')
        sendAuthor = "xxzxaqyw@haaic.gov.cn"
        print datetime.date.today()
        try:
            mailServer = smtplib.SMTP(self.mail[0], 25)
            mailServer.login(self.mail[1], self.mail[2])
            mailServer.sendmail(sendAuthor, receiveMailName, message.as_string())
            mailServer.close()
            print u"邮件发送成功"
        except Exception as e:
            print e

    def getCookie(self):
        self.spiderFirefox = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
        self.spiderFirefox.get(self.bugUrl)
        time.sleep(5)
        cookies = ""
        for cookie in self.spiderFirefox.get_cookies():
            cookies += u"%s=%s; "%(cookie["name"], cookie["value"])
        self.spiderFirefox.close()
        return cookies

    def checkResponseBug(self):
        """
        @函数方法:函数检测今日是否有漏洞，无漏洞发送管理员，有漏洞全体发送
        :return: 
        """
        if self.getDateUpdate(self.getUrlResponse_Result()) == []:
            self.sendMail(receiveMailName=adminList(), receiveAuthor=adminList(), code=1)
        else:
            self.sendMail(receiveMailName=userlist(), receiveAuthor=userlist())

if __name__ == "__main__":
    from apscheduler.schedulers.blocking import BlockingScheduler
    from datetime import date
    logging.basicConfig()
    try:
        sched = BlockingScheduler()
        a = BugSpider()
        a.checkResponseBug()
        #job = sched.add_job(a.checkResponseBug, 'interval', seconds=60)
        # job = sched.add_job(a.checkResponseBug, 'cron', hour='10,12,15,17,18', minute="10", second="0")
        sched.start()
    except Exception as e:
        print e