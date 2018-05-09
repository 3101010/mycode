#coding=utf8
import os
import requests
import json
import sys

access_token=""
ip_list=[]
port_list=[]
def login():
	username=raw_input("input username:")
	passwd=raw_input("input password:")
	data={'username':username,'password':passwd}
	data_encoded=json.dumps(data)
	try:
		m=requests.post(url="https://api.zoomeye.org/user/login",data=data_encoded)
		m_decode=json.loads(m.text)
		global access_token
		access_token=m_decode['access_token']
	except Exception,e:
		print "Error"
		exit()
def Asearch(cmds):
	print cmds
	page=1
	headers={'Authorization':'JWT '+access_token,}
	while True:
		try:					
			m=requests.get(url='http://api.zoomeye.org/host/search?query='+cmds+'&facet=app,os&page='+str(page),headers=headers)
			m_decode=json.loads(m.text)
			for x in m_decode['matches']:
				print '%s:%s' % (x['ip'],x['portinfo']['port'])
				ip_list.append(x['ip'])	
				port_list.append(x['portinfo']['port'])
		except KeyboardInterrupt:
			print "Stopping!!!"
			exit()
		except Exception,e:
			print "Done!!!"
			break
		else:
			page+=1
def main():
	'''Usage:
	python xxx.py "Search Content"'''
	try:
		cmds=str(sys.argv[1])
		login()
		Asearch(cmds)
		nvs=zip(ip_list,port_list)
		nvDict=dict((ip,port) for ip,port in nvs)		
		with open('iplist.txt','w') as f:
				for key in nvDict:
					line=str(key)+':'+str(nvDict[key])+'\n'						
					f.write(line)
	except IndexError,e:
		print "Error:Check the value of the content!"+'\n'+main.__doc__
if __name__=='__main__':	
	main()
	
	
