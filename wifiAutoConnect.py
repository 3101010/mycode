#!/usr/bin/env python
# coding: gb2312
__author__ = 'Elva'
 
import os
import time
import sys
#import datetime
 
from time import localtime, strftime
 
###每N分钟检查一次网络,如果断开进行重连
#f_handler=open('net_check.log', 'w')
#sys.stdout=f_handler
 
#ISOFORMAT='%Y-%m-%d %H:%M:%S' #设置输出格式
 
# isinstance(c,int)
# 
CAO_NI_MA3 = '''
  　                                  　　　　┏┓　　　┏┓    
  　                                  　　　┏┛┻━━━┻┗┓  
  　                                  　　　┃　　　　　　　┃  
  　                                  　　　┃　　　━　　　┃  
  　                                  　　　┃　┳┛　┗┳　┃  
  　                                  　　　┃　　　　　　　┃  
  　                                  　　　┃　　　┻　　　┃  
  　                                  　　　┗━┓  神  ┏━┛  
  　                                  　　　　　┃　兽  ┃      
  　                                  　┏━━━┛　佑　┃      
  　                                  ┏┛          护  ┃      
  　                                  ┗┓              ┃      
  　                                  　┗┓┏┳━┓┏┏┛      
  　                                  　　┣┣┃　┣┣┃        
  　                                  　　┗┻┛　┗┻┛        '''
 
   
CAO_NI_MA = '''
  　　　　　┏┓　　　┏┓    
  　　　　┏┛┻━━━┻┗┓  
  　　　　┃　　　　　　　┃  
  　　　　┃　　　━　　　┃  
  　　　　┃　┳┛　┗┳　┃  
  　　　　┃　　　　　　　┃  
  　　　　┃　　　┻　　　┃  
  　　　　┗━┓      ┏━┛  
  　　　　　　┃　草　┃      
  　　┏━━━┛　尼　┃      
  　┏┛          玛  ┃      
  　┗┓              ┃      
  　　┗┓┏┳━┓┏┏┛      
  　　　┣┣┃　┣┣┃        
  　　　┗┻┛　┗┻┛        '''
def intcCount():
    intc = open("rc_count.txt",'w')
    intc.write("0")
def chcCount():
    '''计数+1'''
    fh = open("rc_count.txt",'w+')
    count_ = fh.read()
    print count_
    count_ = int(count_)
    count_ = count_ + 1
    #print count_
    fh.seek(0)
    fh.write(str(count_))
    fh.close()
 
def log(text):
    ''' 记录日志'''
    #global ISOFORMAT
    #now = datetime.datetime.now()
    nowStr = strftime("%Y-%m-%d %H:%M:%S", localtime());
    msg = nowStr + " : " + text
    print(msg)
    fh = open("_netcheck.log",'a')
    fh.write(msg + "\n")
    fh.close()
log("********************【--GOOD_LUCK--】********************")
log(CAO_NI_MA3)
log("********************【--GOOD_LUCK--】********************")
#log("qcc")
     
#等待多少秒
def wait(s):
    ''' 等待S秒'''
    #print("---------------------SLEEP(%ss)--------------------" %s)
    if s <= 0:
        return
    i = s*2-1;
    while i > 0:
        i=i-1
        time.sleep(0.5)
        print '.',
    time.sleep(0.5)
    print '.'
    #print("---------------------SLEEP(%ss)-------------------" %s)
#wait(3)
#检查网络计数
check_net_count = 0
#重连计数
reconnect_count = 0
#域名索引
domain_index = 0
def check_net():
    '''检查网络'''
    print("");
    global check_net_count
    global reconnect_count
    global domain_index
    check_net_count=check_net_count+1
    log("---------------------CHECK_NET_STA(%d)---------------------" %check_net_count)
    #ping_list =["www.qq.com","www.163.com","www.sohu.com"]
    ping_list =["www.baidu.com","www.163.com","www.qq.com"]
    #ping_list =["www.baidu.com","www.qq.com","www.163.com","www.sohu.com","www.sina.com","www.oschina.net"]
    ping_str = "ping -n 1 " + ping_list[(domain_index)%(len(ping_list))]
    log("INFO:PING:["+ ping_list[(domain_index)%(len(ping_list))] +"]...")
    domain_index = domain_index + 1;
    #ret = os.system("ping www.qq.com")
    ret = os.system(ping_str)
    log("INFO:PING STATUS_CODE:%d" %ret)
    if ret:
        #try again
        log("WARN:NET MAY DOWN,try2 next domain!!!")
        #time.sleep(5)#暂停N秒
        wait(3)
        ping_str = "ping " + ping_list[(domain_index)%(len(ping_list))]
        log("INFO:PING2:["+ ping_list[(domain_index)%(len(ping_list))] +"]...")
        domain_index = domain_index + 1; # domain_index+=1
        ret = os.system(ping_str)
        log("INFO:PING2 STATUS_CODE:%d" %ret)
        if ret:
            #try again
            log("WARN:NET MAY DOWN,try3 next domain!!!")
            #time.sleep(5)#暂停N秒
            wait(3)
            ping_str = "ping " + ping_list[(domain_index)%(len(ping_list))]
            log("INFO:PING3:["+ ping_list[(domain_index)%(len(ping_list))] +"]...")
            domain_index = domain_index + 1; # domain_index+=1
            ret = os.system(ping_str)
            log("INFO:PING3 STATUS_CODE:%d" %ret)
    if not ret:
        log("INFO:NET IS OK (RC=%d)!!" %reconnect_count)
        log("---------------------CHECK_NET_END(%d)---------------------\n" %check_net_count)
    else:
        print(CAO_NI_MA)
        log("FUCK:NET IS DOWN!")
         
        reconnect_count = reconnect_count + 1
        chcCount()
        log("INFO:尝试断开重连(%d)..." %reconnect_count);
        #先断开连接
        log("INFO:尝试断开连接...");
        netsh_ret = os.system("netsh wlan disconnect")
        # netsh_ret1 = os.system('netsh interface set interface "以太网" disabled')
        wait(3)
        log("INFO:尝试重新连接...");
        netsh_ret = os.system("netsh wlan connect name=xxzx708")
        # netsh_ret1 = os.system('netsh interface set interface "以太网" enabled')
        #wait(2)
        log("INFO:NETSH_RET STATUS_CODE:%d" %netsh_ret)
        log("---------------------CHECK_NET_END(%d)---------------------\n" %check_net_count)
 
intcCount()
while True:
    check_net()
    time.sleep(5)#每五分钟PING一次
    #time.sleep(10)#每五分钟PING一次
