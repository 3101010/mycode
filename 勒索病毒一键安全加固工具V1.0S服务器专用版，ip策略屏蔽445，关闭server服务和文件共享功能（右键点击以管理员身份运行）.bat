@echo off
mode con: cols=84 lines=30
:ICSP
title  �����������һ����ȫ�ӹ̹���V1.0S������ר�ð�
color 0A
cls                 
echo.                      
echo ---------------  �����������һ����ȫ�ӹ̹���V1.0S������ר�ð�  --------------------                                                                     
echo                              ����绰9640 ,708��
echo ------------------------------------------------------------------------------------          
echo              *��������ɼ���Ӳ���ļ����ܺ��߱���֧���߶������п��ܽ��ָܻ�
echo              ����ȫ���ոߣ�Ӱ�췶Χ�㣡
echo.     
echo              * ������ϵͳ����Ա������С�
echo              * ���нű��󽫹ر�server����WMI����
echo              * ���нű��󽫿���IP��ȫ��������135��137��138��139��445�˿ڡ�
echo              * �ر�server���񽫲���ʹ�þ������ļ������ܣ�Ϊ�˰�ȫ��رա�
echo              * �ر�WMI������ܵ��¼��ٲ���������ܲ����ã���ȷʵ��Ҫ�ٿ�����
echo              * �ð汾�������ڷ������ӹ̣����Ὺ������ǽ����Ӱ��ҵ��                                                                                                                              
echo ------------------------------------------------------------------------------------
setlocal enabledelayedexpansion
for /f "delims=" %%a in ('ver') do (
	set version=%%a
	set version=!version:~-9,3!
	if "!version!" equ "6.1" (
		echo ��⵽����Win7��Win2008����ϵͳ����ʼ�ӹ�.....��ȴ������360�Ȱ�ȫ�������������
		goto WIN7WIN8WIN1020082016
	) else if "!version!" equ "6.0" (
		echo ��⵽����Vista����ϵͳ����ʼ�ӹ�.....��ȴ������360�Ȱ�ȫ�������������
		goto WIN7WIN8WIN1020082016
	) else if "!version!" equ "6.2" (
		echo ��⵽����Win8��Win2012����ϵͳ����ʼ�ӹ�.....��ȴ������360�Ȱ�ȫ�������������
		goto WIN7WIN8WIN1020082016
	) else if "!version!" equ ".0." (
		echo ��⵽����Win10��Win2016����ϵͳ����ʼ�ӹ�.....��ȴ������360�Ȱ�ȫ�������������
		goto WIN7WIN8WIN1020082016
	) else if "!version!" equ "5.2" (
		echo ��⵽����Win 2003����ϵͳ����ʼ�ӹ�.....��ȴ������360�Ȱ�ȫ�������������
		goto WIN2003
	) else if "!version!" equ "5.1" (
		echo ��⵽����WinXP����ϵͳ����ʼ�ӹ�.....��ȴ������360�Ȱ�ȫ�������������
		goto XP

	) else (
		echo ����ϵͳ��֧��һ���ӹ̣�����ϵ��ȫ����Ա9640
	)
)
:XP
net stop server /Y > nul 2> nul
sc config LanmanServer start= Disabled > nul 2> nul
sc config Winmgmt start= enable > nul 2> nul 
net start Winmgmt /Y > nul 2> nul
echo -------------------------------------------------------------------------------------
echo    * ��ϲ������ϵͳ�Ѽӹ̳ɹ�����رմ��ڼ��ɣ�
pause
goto quit
:WIN2003
net stop server > nul 2> nul
sc config lanmanserver start= disabled > nul 2> nul
net stop Winmgmt /Y > nul 2> nul
sc config Winmgmt start= Disabled > nul 2> nul
echo ---------------------------------------------------------------------------------
echo ��������IP��ȫ���ԣ�����135��137��138��139��445�˿ڡ�             
netsh ipsec static add policy name=�������Σ�ն˿�
netsh ipsec static add filterlist name=Port > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=135 protocol=TCP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=137 protocol=TCP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=138 protocol=TCP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=139 protocol=TCP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=445 protocol=TCP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=135 protocol=UDP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=137 protocol=UDP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=138 protocol=UDP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=139 protocol=UDP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=445 protocol=UDP > nul
netsh ipsec static add filteraction name=Blocked-Access action=block > nul
netsh ipsec static add rule name=Rule1 policy=�������Σ�ն˿� filterlist=Port filteraction=Blocked-Access > nul
netsh ipsec static set policy name=�������Σ�ն˿� assign=y > nul
echo    * ��ϲ������ϵͳ�Ѽӹ̳ɹ�����رմ��ڼ��ɣ�
pause
goto quit
:WIN7WIN8WIN1020082016
net stop server /Y > nul 2> nul
sc config LanmanServer start= Disabled > nul 2> nul
net stop Winmgmt /Y > nul 2> nul
sc config Winmgmt start= Disabled > nul 2> nul
echo -----------------------------------------------------------------------------------
echo ��������IP��ȫ���ԣ�����135��137��138��139��445�˿ڡ�             
netsh ipsec static add policy name=�������Σ�ն˿�
netsh ipsec static add filterlist name=Port
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=135 protocol=TCP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=137 protocol=TCP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=138 protocol=TCP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=139 protocol=TCP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=445 protocol=TCP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=135 protocol=UDP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=137 protocol=UDP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=138 protocol=UDP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=139 protocol=UDP > nul
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=445 protocol=UDP > nul
netsh ipsec static add filteraction name=Blocked-Access action=block
netsh ipsec static add rule name=Rule1 policy=�������Σ�ն˿� filterlist=Port filteraction=Blocked-Access
netsh ipsec static set policy name=�������Σ�ն˿� assign=y
echo    * ��ϲ������ϵͳ�Ѽӹ̳ɹ�����رմ��ڼ��ɣ�
pause
goto quit