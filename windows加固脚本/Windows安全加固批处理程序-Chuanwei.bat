cls
@color 0A
:menu
@mode con cols=80 lines=32
@title 金盾Windwos安全加固 - - - Windows 7 / Windows 2008 通用版
:menu
mode con cols=100 lines=100
@echo off
echo ===============================================================================
echo ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
@echo off
echo ※金盾Windwos安全加固 - - - Windows 7 / Windows 2008 通用版※ 
@echo off
echo ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
@echo off
echo ===============================================================================
@echo off
echo.
echo 请临时关闭360等杀毒软件！
pause

echo 【一、身份鉴别】

echo a.开启帐户密码复杂性要求
echo [version] >Chuanwei.inf
echo signature="$CHICAGO$" >>Chuanwei.inf
echo [System Access] >>Chuanwei.inf
echo PasswordComplexity=1 >>Chuanwei.inf  
::修改帐户密码最小长度为8
echo MinimumPasswordLength=8 >>Chuanwei.inf  
::修改帐户密码最长留存期为90天
echo MaximumPasswordAge=90 >>Chuanwei.inf 
::密码最短使用期限1天
echo MinimumPasswordAge = 2 >>Chuanwei.inf
::修改强制密码历史为5次
echo PasswordHistorySize=2 >>Chuanwei.inf  
::禁用Guest帐户
echo EnableGuestAccount=0 >>Chuanwei.inf  
::执行脚本
secedit /configure /db Chuanwei.sdb /cfg Chuanwei.inf /log Chuanwei.log /quiet
del Chuanwei.*
 
echo b.账号锁定策略
echo [version] >Chuanwei.inf
echo signature="$CHICAGO$" >>Chuanwei.inf
echo [System Access] >>Chuanwei.inf
echo ResetLockoutCount = 30 >>Chuanwei.inf   
::重置帐户锁定计数器3分钟
echo LockoutDuration = 30 >>Chuanwei.inf   
::帐号锁定时间5分钟
echo LockoutBadCount=3 >>Chuanwei.inf   
::设定帐户锁定阀值为5次

::执行脚本
secedit /configure /db Chuanwei.sdb /cfg Chuanwei.inf /log Chuanwei.log /quiet
del Chuanwei.*

echo 【二、访问控制】
echo a.禁用共享
::禁用自动共享
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v "AutoShareServer" /t "REG_DWORD" /d "0" /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v "AutoShareWKS" /t "REG_DWORD" /d "0" /f
::清除admin$共享
net share admin$ /del
::清除ipc$共享
net share ipc$ /del
::清除所有默认本地盘符共享
for %%a in (C D E F G H I J K L M N O P Q R S T U V W X Y Z) do @(if exist %%a:\nul (net share %%a$ /delete>nul 2>nul) )

echo b.禁止用户开机自动登录
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "AutoAdminLogon" /t REG_DWORD /d "0" /f

echo c.禁止自动播放
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoDriveTypeAutoRun" /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoDriveTypeAutoRun" /t "REG_DWORD" /d "255" /f

echo d.重命名administrator帐户
wmic useraccount where name='Administrator' call Rename Administrator123

echo e.关机：清理虚拟内存页面文件
echo 关机：清理虚拟内存页面文件
@echo Windows Registry Editor Version 5.00>>Chuanwei.reg 
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management]>>Chuanwei.reg 
@echo "ClearPageFileAtShutdown"=dword:1>>Chuanwei.reg
@regedit /s Chuanwei.reg
@del Chuanwei.reg
echo f.启用交互式登录: 不显示最后的用户名
@echo Windows Registry Editor Version 5.00>>Chuanwei.reg 
@echo [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]>>Chuanwei.reg 
@echo "DontDisplayLastUserName"=dword:1>>Chuanwei.reg
@regedit /s Chuanwei.reg
@del Chuanwei.reg
echo 【三、入侵防范】
echo a.禁止远程修改注册表
@echo Windows Registry Editor Version 5.00>>Chuanwei.reg
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurePipeServers\winreg]>>Chuanwei.reg
@echo "RemoteRegAccess"=dword:0>>Chuanwei.reg
@regedit /s Chuanwei.reg
@del Chuanwei.reg

echo b.防止icmp重定向报文的攻击
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters]>>Chuanwei.reg 
@echo "EnableICMPRedirect"=dword:0>>Chuanwei.reg

echo c.禁止ipc空连接
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa]>>Chuanwei.reg 
@echo "restrictanonymous"=dword:1>>Chuanwei.reg
@regedit /s Chuanwei.reg
@del Chuanwei.reg

echo d.操作系统关机策略安全
echo [Privilege Rights] >>Chuanwei.inf
::关闭系统仅指派给Administrators组
echo seshutdownprivilege=Administrators >>Chuanwei.inf
::从远程系统强制关机只指派给Administrators组
echo seremoteshutdownprivilege=Administrators >>Chuanwei.inf
::执行脚本
secedit /configure /db Chuanwei.sdb /cfg Chuanwei.inf /log Chuanwei.log /quiet
del Chuanwei.*

echo e.取消系统失败自动重新启动
@echo Windows Registry Editor Version 5.00>>Chuanwei.reg
@echo [HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Crashcontrol]>>Chuanwei.reg
@echo "AutoReboot"=dword:0>>Chuanwei.reg
@regedit /s Chuanwei.reg
@del Chuanwei.reg

echo 【四、安全审计】

echo a.配置审计策略
echo [version] >Chuanwei.inf
echo signature="$CHICAGO$" >>Chuanwei.inf
echo [Event Audit] >>Chuanwei.inf
::开启审核系统事件
echo AuditSystemEvents=3 >>Chuanwei.inf
::开启审核对象访问
echo AuditObjectAccess=3 >>Chuanwei.inf
::开启审核特权使用
echo AuditPrivilegeUse=3 >>Chuanwei.inf
::开启审核策略更改
echo AuditPolicyChange=3 >>Chuanwei.inf
::开启审核帐户管理
echo AuditAccountManage=3 >>Chuanwei.inf
::开启审核过程跟踪
echo AuditProcessTracking=3 >>Chuanwei.inf
::开启审核目录服务访问
echo AuditDSAccess=3 >>Chuanwei.inf
::开启审核登陆事件
echo AuditLogonEvents=3 >>Chuanwei.inf
::开启审核帐户登陆事件
echo AuditAccountLogon=3 >>Chuanwei.inf

echo b.配置审计日志
echo [System Log] >>Chuanwei.inf
::设置系统日志文件最大500M
echo MaximumLogSize=512000 >>Chuanwei.inf
::设置当达到最大的日志尺寸时按需要改写事件
echo RetentionDays = 180  >>Chuanwei.inf
echo AuditLogRetentionPeriod=1 >>Chuanwei.inf

echo c.配置安全日志
echo [Security Log] >>Chuanwei.inf
::设置安全日志文件最大500M
echo MaximumLogSize=51200 >>Chuanwei.inf
::设置当达到最大的日志尺寸时按需要改写事件
echo RetentionDays = 180  >>Chuanwei.inf
echo AuditLogRetentionPeriod=1 >>Chuanwei.inf

echo d.设置应用日志
echo [Application Log] >>Chuanwei.inf
::设置安全日志文件最大500M
echo MaximumLogSize=51200 >>Chuanwei.inf
::设置当达到最大的日志尺寸时按需要改写事件
echo RetentionDays = 180  >>Chuanwei.inf
echo AuditLogRetentionPeriod=1 >>Chuanwei.inf

::执行脚本
secedit /configure /db Chuanwei.sdb /cfg Chuanwei.inf /log Chuanwei.log /quiet
del Chuanwei.*

echo 【五、资源控制】
echo a.配置屏幕保护时间为10分钟
@echo Windows Registry Editor Version 5.00>>scrsave.reg
@echo [HKEY_CURRENT_USER\Control Panel\Desktop]>>scrsave.reg
@echo "ScreenSaveActive"="1">>scrsave.reg
@echo "ScreenSaverIsSecure"="1">>scrsave.reg
@echo "ScreenSaveTimeOut"="600">>scrsave.reg
@echo "SCRNSAVE.EXE"="c:\\WINDOWS\\system32\\scrnsave.scr">>scrsave.reg
@regedit /s scrsave.reg
@del scrsave.reg

echo b.修改远程桌面端口
::修改3389远程登陆端口号为16000,开启远程设置
@echo Windows Registry Editor Version 5.00>>Wanghualang.reg 
echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server]>>Wanghualang.reg
echo "fDenyTSConnections"=dword:00000000>>Wanghualang.reg
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\Wds\rdpwd\Tds\tcp]>>Wanghualang.reg 
@echo "PortNumber"=dword:3e80>>Wanghualang.reg
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp]>>Wanghualang.reg 
@echo "PortNumber"=dword:3e80>>Wanghualang.reg
@regedit /s Wanghualang.reg
@del Wanghualang.reg
pause

cls
@echo off
echo.   
echo 即将创建IP安全策略，屏蔽135、137、138、139、445端口、关闭server服务。             
echo.   
set /p KEY=  请选择（Y / N）：
echo.
if %KEY% == y    goto IPsec
if %KEY% == n    goto :Firewall1

:IPsec
echo 关闭server服务
net stop server /Y > nul 2> nul
echo 即将创建IP安全策略，屏蔽135、137、138、139、445端口、关闭server服务。
netsh ipsec static add policy name=金盾屏蔽危险端口
netsh ipsec static add filterlist name=Port
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
netsh ipsec static add filteraction name=Blocked-Access action=block
netsh ipsec static add rule name=Rule1 policy=金盾屏蔽危险端口 filterlist=Port filteraction=Blocked-Access
netsh ipsec static set policy name=金盾屏蔽危险端口 assign=y
echo   IP安全策略已完成！

:Firewall1
echo.   
echo 即将打开本地防火墙配置安全策略，屏蔽135、137、138、139、445端口、关闭server服务。（服务器请谨慎开启防火墙）             
echo.   
set /p KEY=  请选择（Y / N）：
echo.
if %KEY% == y    goto Firewall
if %KEY% == n    goto restart

:Firewall
echo 关闭server服务
net stop server /Y > nul 2> nul
echo 即将打开本地防火墙配置安全策略，屏蔽135、137、138、139、445端口、关闭server服务。（服务器请谨慎开启防火墙）
netsh firewall set opmode enable > nul 2> nul
netsh advfirewall set Allprofile state on > nul 2> nul
netsh advfirewall firewall add rule name="金盾屏蔽危险端口TCP" dir=in action=block localport=135,137,138,139,445 remoteip=any protocol=tcp > nul
netsh advfirewall firewall add rule name="金盾屏蔽危险端口UDP" dir=in action=block localport=135,137,138,139,445 remoteip=any protocol=udp > nul

:restart
cls
echo 操作系统安全加固已完成，建议重启计算机生效！现在立即重新启动计算机吗？
echo.
set /p select1=请输入（Y / N）:
if /i "%select1%"=="Y" goto y
if /i "%select1%"=="N" goto n
:y
shutdown -r -t 0
exit
:n
exit