cls
@color 0A
:menu
@mode con cols=80 lines=32
@title 游软轨迹 -王花郎博客 - - - Windows 7 / Windows 2008 通用版
:menu
@echo off
echo ===============================================================================
echo ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
@echo off
echo ※批处理脚本代码均来自论坛网友分享，使用前建议先在虚拟机操作系统中进行完整测试※ 
@echo off
echo ※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※※
@echo off
echo ===============================================================================
@echo off
echo. 
pause



::2.使用星号（*）隐藏共享口令
@echo Windows Registry Editor Version 5.00>>Wanghualang.reg 
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services]>>Wanghualang.reg 
@echo [HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Network]>>Wanghualang.reg 
@echo "HideSharePwds"=dword:1>>Wanghualang.reg
@regedit /s Wanghualang.reg
@del Wanghualang.reg
 




::[禁止用户开机自动登录]
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "AutoAdminLogon" /t REG_DWORD /d "0" /f

::[禁止自动播放]
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoDriveTypeAutoRun" /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoDriveTypeAutoRun" /t "REG_DWORD" /d "255" /f

::[对administrator帐户进行重命名]
wmic useraccount where name='Administrator' call Rename bdgly



::[取消系统失败自动重新启动]
@echo Windows Registry Editor Version 5.00>>Wanghualang.reg
@echo [HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Crashcontrol]>>Wanghualang.reg
@echo "AutoReboot"=dword:0>>Wanghualang.reg
@regedit /s Wanghualang.reg
@del Wanghualang.reg

::【安全审计】
::[配置审计策略]
echo [version] >Wanghualang.inf
echo signature="$CHICAGO$" >>Wanghualang.inf
echo [Event Audit] >>Wanghualang.inf
::开启审核系统事件
echo AuditSystemEvents=3 >>Wanghualang.inf
::开启审核对象访问
echo AuditObjectAccess=3 >>Wanghualang.inf
::开启审核特权使用
echo AuditPrivilegeUse=3 >>Wanghualang.inf
::开启审核策略更改
echo AuditPolicyChange=3 >>Wanghualang.inf
::开启审核帐户管理
echo AuditAccountManage=3 >>Wanghualang.inf
::开启审核过程跟踪
echo AuditProcessTracking=3 >>Wanghualang.inf
::开启审核目录服务访问
echo AuditDSAccess=3 >>Wanghualang.inf
::开启审核登陆事件
echo AuditLogonEvents=3 >>Wanghualang.inf
::开启审核帐户登陆事件
echo AuditAccountLogon=3 >>Wanghualang.inf
::[配置审计日志]
echo [System Log] >>Wanghualang.inf
::设置系统日志文件最大50M
echo MaximumLogSize=51200 >>Wanghualang.inf
::设置当达到最大的日志尺寸时按需要改写事件
echo RetentionDays = 60  >>Wanghualang.inf
echo AuditLogRetentionPeriod=1 >>Wanghualang.inf

::配置安全日志
echo [Security Log] >>Wanghualang.inf
::设置安全日志文件最大50M
echo MaximumLogSize=51200 >>Wanghualang.inf
::设置当达到最大的日志尺寸时按需要改写事件
echo RetentionDays = 60  >>Wanghualang.inf
echo AuditLogRetentionPeriod=1 >>Wanghualang.inf

::设置应用日志
echo [Application Log] >>Wanghualang.inf
::设置安全日志文件最大50M
echo MaximumLogSize=51200 >>Wanghualang.inf
::设置当达到最大的日志尺寸时按需要改写事件
echo RetentionDays = 60  >>Wanghualang.inf
echo AuditLogRetentionPeriod=1 >>Wanghualang.inf

::执行脚本
secedit /configure /db Wanghualang.sdb /cfg Wanghualang.inf /log Wanghualang.log /quiet
del Wanghualang.*

::【入侵防范】
::[b.防止SYN FLOOD 攻击]
@echo Windows Registry Editor Version 5.00>>Wanghualang.reg 
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services]>>Wanghualang.reg 
@echo "SynAttackProtect"=dword:2>>Wanghualang.reg
@echo "TcpMaxPortsExhausted"=dword:5>>Wanghualang.reg
@echo "TcpMaxHalfOpen"=dword:1f4>>Wanghualang.reg
@echo "TcpMaxHalfOpenRetried"=dword:190>>Wanghualang.reg

::[c.防止icmp重定向报文的攻击]
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters]>>Wanghualang.reg 
@echo "EnableICMPRedirect"=dword:0>>Wanghualang.reg

::[d.禁止ipc空连接]
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa]>>Wanghualang.reg 
@echo "restrictanonymous"=dword:1>>Wanghualang.reg
@regedit /s Wanghualang.reg
@del Wanghualang.reg

::[f.操作系统关机策略安全]
echo [Privilege Rights] >>Wanghualang.inf
::1.关闭系统仅指派给Administrators组
echo seshutdownprivilege=Administrators >>Wanghualang.inf
::2.从远程系统强制关机只指派给Administrators组
echo seremoteshutdownprivilege=Administrators >>Wanghualang.inf
::执行脚本
secedit /configure /db Wanghualang.sdb /cfg Wanghualang.inf /log Wanghualang.log /quiet
del Wanghualang.*

::[g.操作系统数据执行保护安全]
::开启仅为基本 Windows 程序和服务启用DEP
bcdedit /set nx optin

::[h.关闭系统自带防火墙]
::关闭防火墙(公用、专用）
netsh advfirewall set currentprofile state off
netsh advfirewall set privateprofile state off

::【资源控制】
::[b.根据安全策略设置登录终端的操作超时锁定]
::2.启用远程会话挂起时间限制
@echo Windows Registry Editor Version 5.00>>Wanghualang.reg 
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services]>>Wanghualang.reg 
echo [HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters]>>Wanghualang.reg
@echo "autodisconnect"=dword:a >>Wanghualang.reg
::设置暂停会话前所需的空闲时间量 10分钟
@regedit /s Wanghualang.reg
@del Wanghualang.reg

::3.屏幕保护时间为三分钟
@echo Windows Registry Editor Version 5.00>>scrsave.reg
@echo [HKEY_CURRENT_USER\Control Panel\Desktop]>>scrsave.reg
@echo "ScreenSaveActive"="1">>scrsave.reg
@echo "ScreenSaverIsSecure"="1">>scrsave.reg
@echo "ScreenSaveTimeOut"="180">>scrsave.reg
@echo "SCRNSAVE.EXE"="c:\\WINDOWS\\system32\\scrnsave.scr">>scrsave.reg
@regedit /s scrsave.reg
@del scrsave.reg

::【远程设置策略】
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
echo 即将创建IP安全策略，屏蔽135、137、138、139、445、3389端口。             
echo.   
set /p KEY=  请选择（Y / N）：
echo.
if %KEY% == y    goto IPsec
if %KEY% == n    goto IP

:IPsec 
netsh ipsec static add policy name=Shield-Port
netsh ipsec static add filterlist name=Port
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=135 protocol=TCP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=137 protocol=TCP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=138 protocol=TCP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=139 protocol=TCP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=445 protocol=TCP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=3389 protocol=TCP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=135 protocol=UDP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=137 protocol=UDP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=138 protocol=UDP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=139 protocol=UDP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=445 protocol=UDP
netsh ipsec static add filter filterlist=Port srcaddr=any dstaddr=Me dstport=3389 protocol=UDP
netsh ipsec static add filteraction name=Blocked-Access action=block
netsh ipsec static add rule name=Rule1 policy=Shield-Port filterlist=Port filteraction=Blocked-Access
netsh ipsec static set policy name=Shield-Port assign=y

::【计算机名与IP地址设置】
:IP
cls
@echo off   
echo.   
echo 1.修改计算机名                        
echo.   
echo 2.修改计算机IP地址                               
echo. 
echo 3.不修改任何信息   
echo.
set /p KEY=  请选择：
echo.
if %KEY% == 1    goto ONE  
if %KEY% == 2    goto TWO  
if %KEY% == 3    goto NO

:ONE
echo.
set /p name=  计算机名:
echo.
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\ShellNoRoam" /v @ /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName" /v "ComputerName" /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Control\ComputerName\ActiveComputerName" /v "ComputerName" /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Services\Eventlog" /v "ComputerName" /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName" /v "ComputerName" /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "NV Hostname" /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "Hostname" /t REG_SZ /d "%name%" /f >nul
goto IP

:TWO
set NAME="本地连接"
echo.    
set /p IP= [请输入本机IP地址] 
echo.     
set /p MASK= [请输入子网掩码地址] 
echo.    
set /p GATEWAY= [请输入默认网关地址]  
echo.
netsh interface ip set address %NAME% static %IP% %MASK% %GATEWAY%  
netsh interface ip add dns %NAME%  114.114.114.114
netsh interface ip add dns %NAME%  114.114.114.119
goto IP

:NO
goto restart

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