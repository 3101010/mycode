cls
@color 0A
:menu
@mode con cols=80 lines=32
@title ���Windwos��ȫ�ӹ� - - - Windows 7 / Windows 2008 ͨ�ð�
:menu
mode con cols=100 lines=100
@echo off
echo ===============================================================================
echo ��������������������������������������������������������������������������������
@echo off
echo �����Windwos��ȫ�ӹ� - - - Windows 7 / Windows 2008 ͨ�ð�� 
@echo off
echo ��������������������������������������������������������������������������������
@echo off
echo ===============================================================================
@echo off
echo.
echo ����ʱ�ر�360��ɱ�������
pause

echo ��һ����ݼ���

echo a.�����ʻ����븴����Ҫ��
echo [version] >Chuanwei.inf
echo signature="$CHICAGO$" >>Chuanwei.inf
echo [System Access] >>Chuanwei.inf
echo PasswordComplexity=1 >>Chuanwei.inf  
::�޸��ʻ�������С����Ϊ8
echo MinimumPasswordLength=8 >>Chuanwei.inf  
::�޸��ʻ������������Ϊ90��
echo MaximumPasswordAge=90 >>Chuanwei.inf 
::�������ʹ������1��
echo MinimumPasswordAge = 2 >>Chuanwei.inf
::�޸�ǿ��������ʷΪ5��
echo PasswordHistorySize=2 >>Chuanwei.inf  
::����Guest�ʻ�
echo EnableGuestAccount=0 >>Chuanwei.inf  
::ִ�нű�
secedit /configure /db Chuanwei.sdb /cfg Chuanwei.inf /log Chuanwei.log /quiet
del Chuanwei.*
 
echo b.�˺���������
echo [version] >Chuanwei.inf
echo signature="$CHICAGO$" >>Chuanwei.inf
echo [System Access] >>Chuanwei.inf
echo ResetLockoutCount = 30 >>Chuanwei.inf   
::�����ʻ�����������3����
echo LockoutDuration = 30 >>Chuanwei.inf   
::�ʺ�����ʱ��5����
echo LockoutBadCount=3 >>Chuanwei.inf   
::�趨�ʻ�������ֵΪ5��

::ִ�нű�
secedit /configure /db Chuanwei.sdb /cfg Chuanwei.inf /log Chuanwei.log /quiet
del Chuanwei.*

echo ���������ʿ��ơ�
echo a.���ù���
::�����Զ�����
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v "AutoShareServer" /t "REG_DWORD" /d "0" /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v "AutoShareWKS" /t "REG_DWORD" /d "0" /f
::���admin$����
net share admin$ /del
::���ipc$����
net share ipc$ /del
::�������Ĭ�ϱ����̷�����
for %%a in (C D E F G H I J K L M N O P Q R S T U V W X Y Z) do @(if exist %%a:\nul (net share %%a$ /delete>nul 2>nul) )

echo b.��ֹ�û������Զ���¼
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "AutoAdminLogon" /t REG_DWORD /d "0" /f

echo c.��ֹ�Զ�����
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoDriveTypeAutoRun" /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoDriveTypeAutoRun" /t "REG_DWORD" /d "255" /f

echo d.������administrator�ʻ�
wmic useraccount where name='Administrator' call Rename Administrator123

echo e.�ػ������������ڴ�ҳ���ļ�
echo �ػ������������ڴ�ҳ���ļ�
@echo Windows Registry Editor Version 5.00>>Chuanwei.reg 
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management]>>Chuanwei.reg 
@echo "ClearPageFileAtShutdown"=dword:1>>Chuanwei.reg
@regedit /s Chuanwei.reg
@del Chuanwei.reg
echo f.���ý���ʽ��¼: ����ʾ�����û���
@echo Windows Registry Editor Version 5.00>>Chuanwei.reg 
@echo [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]>>Chuanwei.reg 
@echo "DontDisplayLastUserName"=dword:1>>Chuanwei.reg
@regedit /s Chuanwei.reg
@del Chuanwei.reg
echo ���������ַ�����
echo a.��ֹԶ���޸�ע���
@echo Windows Registry Editor Version 5.00>>Chuanwei.reg
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurePipeServers\winreg]>>Chuanwei.reg
@echo "RemoteRegAccess"=dword:0>>Chuanwei.reg
@regedit /s Chuanwei.reg
@del Chuanwei.reg

echo b.��ֹicmp�ض����ĵĹ���
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters]>>Chuanwei.reg 
@echo "EnableICMPRedirect"=dword:0>>Chuanwei.reg

echo c.��ֹipc������
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa]>>Chuanwei.reg 
@echo "restrictanonymous"=dword:1>>Chuanwei.reg
@regedit /s Chuanwei.reg
@del Chuanwei.reg

echo d.����ϵͳ�ػ����԰�ȫ
echo [Privilege Rights] >>Chuanwei.inf
::�ر�ϵͳ��ָ�ɸ�Administrators��
echo seshutdownprivilege=Administrators >>Chuanwei.inf
::��Զ��ϵͳǿ�ƹػ�ָֻ�ɸ�Administrators��
echo seremoteshutdownprivilege=Administrators >>Chuanwei.inf
::ִ�нű�
secedit /configure /db Chuanwei.sdb /cfg Chuanwei.inf /log Chuanwei.log /quiet
del Chuanwei.*

echo e.ȡ��ϵͳʧ���Զ���������
@echo Windows Registry Editor Version 5.00>>Chuanwei.reg
@echo [HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Crashcontrol]>>Chuanwei.reg
@echo "AutoReboot"=dword:0>>Chuanwei.reg
@regedit /s Chuanwei.reg
@del Chuanwei.reg

echo ���ġ���ȫ��ơ�

echo a.������Ʋ���
echo [version] >Chuanwei.inf
echo signature="$CHICAGO$" >>Chuanwei.inf
echo [Event Audit] >>Chuanwei.inf
::�������ϵͳ�¼�
echo AuditSystemEvents=3 >>Chuanwei.inf
::������˶������
echo AuditObjectAccess=3 >>Chuanwei.inf
::���������Ȩʹ��
echo AuditPrivilegeUse=3 >>Chuanwei.inf
::������˲��Ը���
echo AuditPolicyChange=3 >>Chuanwei.inf
::��������ʻ�����
echo AuditAccountManage=3 >>Chuanwei.inf
::������˹��̸���
echo AuditProcessTracking=3 >>Chuanwei.inf
::�������Ŀ¼�������
echo AuditDSAccess=3 >>Chuanwei.inf
::������˵�½�¼�
echo AuditLogonEvents=3 >>Chuanwei.inf
::��������ʻ���½�¼�
echo AuditAccountLogon=3 >>Chuanwei.inf

echo b.���������־
echo [System Log] >>Chuanwei.inf
::����ϵͳ��־�ļ����500M
echo MaximumLogSize=512000 >>Chuanwei.inf
::���õ��ﵽ������־�ߴ�ʱ����Ҫ��д�¼�
echo RetentionDays = 180  >>Chuanwei.inf
echo AuditLogRetentionPeriod=1 >>Chuanwei.inf

echo c.���ð�ȫ��־
echo [Security Log] >>Chuanwei.inf
::���ð�ȫ��־�ļ����500M
echo MaximumLogSize=51200 >>Chuanwei.inf
::���õ��ﵽ������־�ߴ�ʱ����Ҫ��д�¼�
echo RetentionDays = 180  >>Chuanwei.inf
echo AuditLogRetentionPeriod=1 >>Chuanwei.inf

echo d.����Ӧ����־
echo [Application Log] >>Chuanwei.inf
::���ð�ȫ��־�ļ����500M
echo MaximumLogSize=51200 >>Chuanwei.inf
::���õ��ﵽ������־�ߴ�ʱ����Ҫ��д�¼�
echo RetentionDays = 180  >>Chuanwei.inf
echo AuditLogRetentionPeriod=1 >>Chuanwei.inf

::ִ�нű�
secedit /configure /db Chuanwei.sdb /cfg Chuanwei.inf /log Chuanwei.log /quiet
del Chuanwei.*

echo ���塢��Դ���ơ�
echo a.������Ļ����ʱ��Ϊ10����
@echo Windows Registry Editor Version 5.00>>scrsave.reg
@echo [HKEY_CURRENT_USER\Control Panel\Desktop]>>scrsave.reg
@echo "ScreenSaveActive"="1">>scrsave.reg
@echo "ScreenSaverIsSecure"="1">>scrsave.reg
@echo "ScreenSaveTimeOut"="600">>scrsave.reg
@echo "SCRNSAVE.EXE"="c:\\WINDOWS\\system32\\scrnsave.scr">>scrsave.reg
@regedit /s scrsave.reg
@del scrsave.reg

echo b.�޸�Զ������˿�
::�޸�3389Զ�̵�½�˿ں�Ϊ16000,����Զ������
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
echo ��������IP��ȫ���ԣ�����135��137��138��139��445�˿ڡ��ر�server����             
echo.   
set /p KEY=  ��ѡ��Y / N����
echo.
if %KEY% == y    goto IPsec
if %KEY% == n    goto :Firewall1

:IPsec
echo �ر�server����
net stop server /Y > nul 2> nul
echo ��������IP��ȫ���ԣ�����135��137��138��139��445�˿ڡ��ر�server����
netsh ipsec static add policy name=�������Σ�ն˿�
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
netsh ipsec static add rule name=Rule1 policy=�������Σ�ն˿� filterlist=Port filteraction=Blocked-Access
netsh ipsec static set policy name=�������Σ�ն˿� assign=y
echo   IP��ȫ��������ɣ�

:Firewall1
echo.   
echo �����򿪱��ط���ǽ���ð�ȫ���ԣ�����135��137��138��139��445�˿ڡ��ر�server���񡣣��������������������ǽ��             
echo.   
set /p KEY=  ��ѡ��Y / N����
echo.
if %KEY% == y    goto Firewall
if %KEY% == n    goto restart

:Firewall
echo �ر�server����
net stop server /Y > nul 2> nul
echo �����򿪱��ط���ǽ���ð�ȫ���ԣ�����135��137��138��139��445�˿ڡ��ر�server���񡣣��������������������ǽ��
netsh firewall set opmode enable > nul 2> nul
netsh advfirewall set Allprofile state on > nul 2> nul
netsh advfirewall firewall add rule name="�������Σ�ն˿�TCP" dir=in action=block localport=135,137,138,139,445 remoteip=any protocol=tcp > nul
netsh advfirewall firewall add rule name="�������Σ�ն˿�UDP" dir=in action=block localport=135,137,138,139,445 remoteip=any protocol=udp > nul

:restart
cls
echo ����ϵͳ��ȫ�ӹ�����ɣ����������������Ч�������������������������
echo.
set /p select1=�����루Y / N��:
if /i "%select1%"=="Y" goto y
if /i "%select1%"=="N" goto n
:y
shutdown -r -t 0
exit
:n
exit