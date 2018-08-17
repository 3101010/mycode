@echo off
mode con: cols=84 lines=30
:ICSP
title  金盾勒索病毒一键安全加固工具V1.0S服务器专用版
color 0A
cls                 
echo.                      
echo ---------------  金盾勒索病毒一键安全加固工具V1.0S服务器专用版  --------------------                                                                     
echo                              服务电话9640 ,708室
echo ------------------------------------------------------------------------------------          
echo              *勒索软件可加密硬盘文件，受害者必须支付高额赎金才有可能解密恢复
echo              ，安全风险高，影响范围广！
echo.     
echo              * 必须以系统管理员身份运行。
echo              * 运行脚本后将关闭server服务、WMI服务。
echo              * 运行脚本后将开启IP安全策略屏蔽135、137、138、139、445端口。
echo              * 关闭server服务将不能使用局域网文件共享功能，为了安全请关闭。
echo              * 关闭WMI服务可能导致极少部分软件功能不可用，若确实需要再开启。
echo              * 该版本仅可用于服务器加固，不会开启防火墙，不影响业务。                                                                                                                              
echo ------------------------------------------------------------------------------------
setlocal enabledelayedexpansion
for /f "delims=" %%a in ('ver') do (
	set version=%%a
	set version=!version:~-9,3!
	if "!version!" equ "6.1" (
		echo 检测到您是Win7或Win2008操作系统，开始加固.....请等待，如果360等安全软件拦截请允许！
		goto WIN7WIN8WIN1020082016
	) else if "!version!" equ "6.0" (
		echo 检测到您是Vista操作系统，开始加固.....请等待，如果360等安全软件拦截请允许！
		goto WIN7WIN8WIN1020082016
	) else if "!version!" equ "6.2" (
		echo 检测到您是Win8或Win2012操作系统，开始加固.....请等待，如果360等安全软件拦截请允许！
		goto WIN7WIN8WIN1020082016
	) else if "!version!" equ ".0." (
		echo 检测到您是Win10或Win2016操作系统，开始加固.....请等待，如果360等安全软件拦截请允许！
		goto WIN7WIN8WIN1020082016
	) else if "!version!" equ "5.2" (
		echo 检测到您是Win 2003操作系统，开始加固.....请等待，如果360等安全软件拦截请允许！
		goto WIN2003
	) else if "!version!" equ "5.1" (
		echo 检测到您是WinXP操作系统，开始加固.....请等待，如果360等安全软件拦截请允许！
		goto XP

	) else (
		echo 您的系统不支持一键加固，请联系安全管理员9640
	)
)
:XP
net stop server /Y > nul 2> nul
sc config LanmanServer start= Disabled > nul 2> nul
sc config Winmgmt start= enable > nul 2> nul 
net start Winmgmt /Y > nul 2> nul
echo -------------------------------------------------------------------------------------
echo    * 恭喜，您的系统已加固成功，请关闭窗口即可！
pause
goto quit
:WIN2003
net stop server > nul 2> nul
sc config lanmanserver start= disabled > nul 2> nul
net stop Winmgmt /Y > nul 2> nul
sc config Winmgmt start= Disabled > nul 2> nul
echo ---------------------------------------------------------------------------------
echo 即将创建IP安全策略，屏蔽135、137、138、139、445端口。             
netsh ipsec static add policy name=金盾屏蔽危险端口
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
netsh ipsec static add rule name=Rule1 policy=金盾屏蔽危险端口 filterlist=Port filteraction=Blocked-Access > nul
netsh ipsec static set policy name=金盾屏蔽危险端口 assign=y > nul
echo    * 恭喜，您的系统已加固成功，请关闭窗口即可！
pause
goto quit
:WIN7WIN8WIN1020082016
net stop server /Y > nul 2> nul
sc config LanmanServer start= Disabled > nul 2> nul
net stop Winmgmt /Y > nul 2> nul
sc config Winmgmt start= Disabled > nul 2> nul
echo -----------------------------------------------------------------------------------
echo 即将创建IP安全策略，屏蔽135、137、138、139、445端口。             
netsh ipsec static add policy name=金盾屏蔽危险端口
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
netsh ipsec static add rule name=Rule1 policy=金盾屏蔽危险端口 filterlist=Port filteraction=Blocked-Access
netsh ipsec static set policy name=金盾屏蔽危险端口 assign=y
echo    * 恭喜，您的系统已加固成功，请关闭窗口即可！
pause
goto quit