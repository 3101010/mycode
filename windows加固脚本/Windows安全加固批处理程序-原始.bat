cls
@color 0A
:menu
@mode con cols=80 lines=32
@title ����켣 -�����ɲ��� - - - Windows 7 / Windows 2008 ͨ�ð�
:menu
@echo off
echo ===============================================================================
echo ��������������������������������������������������������������������������������
@echo off
echo ��������ű������������̳���ѷ���ʹ��ǰ�����������������ϵͳ�н����������ԡ� 
@echo off
echo ��������������������������������������������������������������������������������
@echo off
echo ===============================================================================
@echo off
echo. 
pause



::2.ʹ���Ǻţ�*�����ع������
@echo Windows Registry Editor Version 5.00>>Wanghualang.reg 
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services]>>Wanghualang.reg 
@echo [HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Network]>>Wanghualang.reg 
@echo "HideSharePwds"=dword:1>>Wanghualang.reg
@regedit /s Wanghualang.reg
@del Wanghualang.reg
 




::[��ֹ�û������Զ���¼]
reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v "AutoAdminLogon" /t REG_DWORD /d "0" /f

::[��ֹ�Զ�����]
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoDriveTypeAutoRun" /f
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoDriveTypeAutoRun" /t "REG_DWORD" /d "255" /f

::[��administrator�ʻ�����������]
wmic useraccount where name='Administrator' call Rename bdgly



::[ȡ��ϵͳʧ���Զ���������]
@echo Windows Registry Editor Version 5.00>>Wanghualang.reg
@echo [HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Crashcontrol]>>Wanghualang.reg
@echo "AutoReboot"=dword:0>>Wanghualang.reg
@regedit /s Wanghualang.reg
@del Wanghualang.reg

::����ȫ��ơ�
::[������Ʋ���]
echo [version] >Wanghualang.inf
echo signature="$CHICAGO$" >>Wanghualang.inf
echo [Event Audit] >>Wanghualang.inf
::�������ϵͳ�¼�
echo AuditSystemEvents=3 >>Wanghualang.inf
::������˶������
echo AuditObjectAccess=3 >>Wanghualang.inf
::���������Ȩʹ��
echo AuditPrivilegeUse=3 >>Wanghualang.inf
::������˲��Ը���
echo AuditPolicyChange=3 >>Wanghualang.inf
::��������ʻ�����
echo AuditAccountManage=3 >>Wanghualang.inf
::������˹��̸���
echo AuditProcessTracking=3 >>Wanghualang.inf
::�������Ŀ¼�������
echo AuditDSAccess=3 >>Wanghualang.inf
::������˵�½�¼�
echo AuditLogonEvents=3 >>Wanghualang.inf
::��������ʻ���½�¼�
echo AuditAccountLogon=3 >>Wanghualang.inf
::[���������־]
echo [System Log] >>Wanghualang.inf
::����ϵͳ��־�ļ����50M
echo MaximumLogSize=51200 >>Wanghualang.inf
::���õ��ﵽ������־�ߴ�ʱ����Ҫ��д�¼�
echo RetentionDays = 60  >>Wanghualang.inf
echo AuditLogRetentionPeriod=1 >>Wanghualang.inf

::���ð�ȫ��־
echo [Security Log] >>Wanghualang.inf
::���ð�ȫ��־�ļ����50M
echo MaximumLogSize=51200 >>Wanghualang.inf
::���õ��ﵽ������־�ߴ�ʱ����Ҫ��д�¼�
echo RetentionDays = 60  >>Wanghualang.inf
echo AuditLogRetentionPeriod=1 >>Wanghualang.inf

::����Ӧ����־
echo [Application Log] >>Wanghualang.inf
::���ð�ȫ��־�ļ����50M
echo MaximumLogSize=51200 >>Wanghualang.inf
::���õ��ﵽ������־�ߴ�ʱ����Ҫ��д�¼�
echo RetentionDays = 60  >>Wanghualang.inf
echo AuditLogRetentionPeriod=1 >>Wanghualang.inf

::ִ�нű�
secedit /configure /db Wanghualang.sdb /cfg Wanghualang.inf /log Wanghualang.log /quiet
del Wanghualang.*

::�����ַ�����
::[b.��ֹSYN FLOOD ����]
@echo Windows Registry Editor Version 5.00>>Wanghualang.reg 
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services]>>Wanghualang.reg 
@echo "SynAttackProtect"=dword:2>>Wanghualang.reg
@echo "TcpMaxPortsExhausted"=dword:5>>Wanghualang.reg
@echo "TcpMaxHalfOpen"=dword:1f4>>Wanghualang.reg
@echo "TcpMaxHalfOpenRetried"=dword:190>>Wanghualang.reg

::[c.��ֹicmp�ض����ĵĹ���]
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters]>>Wanghualang.reg 
@echo "EnableICMPRedirect"=dword:0>>Wanghualang.reg

::[d.��ֹipc������]
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Lsa]>>Wanghualang.reg 
@echo "restrictanonymous"=dword:1>>Wanghualang.reg
@regedit /s Wanghualang.reg
@del Wanghualang.reg

::[f.����ϵͳ�ػ����԰�ȫ]
echo [Privilege Rights] >>Wanghualang.inf
::1.�ر�ϵͳ��ָ�ɸ�Administrators��
echo seshutdownprivilege=Administrators >>Wanghualang.inf
::2.��Զ��ϵͳǿ�ƹػ�ָֻ�ɸ�Administrators��
echo seremoteshutdownprivilege=Administrators >>Wanghualang.inf
::ִ�нű�
secedit /configure /db Wanghualang.sdb /cfg Wanghualang.inf /log Wanghualang.log /quiet
del Wanghualang.*

::[g.����ϵͳ����ִ�б�����ȫ]
::������Ϊ���� Windows ����ͷ�������DEP
bcdedit /set nx optin

::[h.�ر�ϵͳ�Դ�����ǽ]
::�رշ���ǽ(���á�ר�ã�
netsh advfirewall set currentprofile state off
netsh advfirewall set privateprofile state off

::����Դ���ơ�
::[b.���ݰ�ȫ�������õ�¼�ն˵Ĳ�����ʱ����]
::2.����Զ�̻Ự����ʱ������
@echo Windows Registry Editor Version 5.00>>Wanghualang.reg 
@echo [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services]>>Wanghualang.reg 
echo [HKEY_LOCAL_MACHINE\System\CurrentControlSet\Services\LanManServer\Parameters]>>Wanghualang.reg
@echo "autodisconnect"=dword:a >>Wanghualang.reg
::������ͣ�Ựǰ����Ŀ���ʱ���� 10����
@regedit /s Wanghualang.reg
@del Wanghualang.reg

::3.��Ļ����ʱ��Ϊ������
@echo Windows Registry Editor Version 5.00>>scrsave.reg
@echo [HKEY_CURRENT_USER\Control Panel\Desktop]>>scrsave.reg
@echo "ScreenSaveActive"="1">>scrsave.reg
@echo "ScreenSaverIsSecure"="1">>scrsave.reg
@echo "ScreenSaveTimeOut"="180">>scrsave.reg
@echo "SCRNSAVE.EXE"="c:\\WINDOWS\\system32\\scrnsave.scr">>scrsave.reg
@regedit /s scrsave.reg
@del scrsave.reg

::��Զ�����ò��ԡ�
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
echo ��������IP��ȫ���ԣ�����135��137��138��139��445��3389�˿ڡ�             
echo.   
set /p KEY=  ��ѡ��Y / N����
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

::�����������IP��ַ���á�
:IP
cls
@echo off   
echo.   
echo 1.�޸ļ������                        
echo.   
echo 2.�޸ļ����IP��ַ                               
echo. 
echo 3.���޸��κ���Ϣ   
echo.
set /p KEY=  ��ѡ��
echo.
if %KEY% == 1    goto ONE  
if %KEY% == 2    goto TWO  
if %KEY% == 3    goto NO

:ONE
echo.
set /p name=  �������:
echo.
reg add "HKEY_CURRENT_USER\Software\Microsoft\Windows\ShellNoRoam" /v @ /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName" /v "ComputerName" /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Control\ComputerName\ActiveComputerName" /v "ComputerName" /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Services\Eventlog" /v "ComputerName" /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Control\ComputerName\ComputerName" /v "ComputerName" /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "NV Hostname" /t REG_SZ /d "%name%" /f >nul && reg add "HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters" /v "Hostname" /t REG_SZ /d "%name%" /f >nul
goto IP

:TWO
set NAME="��������"
echo.    
set /p IP= [�����뱾��IP��ַ] 
echo.     
set /p MASK= [���������������ַ] 
echo.    
set /p GATEWAY= [������Ĭ�����ص�ַ]  
echo.
netsh interface ip set address %NAME% static %IP% %MASK% %GATEWAY%  
netsh interface ip add dns %NAME%  114.114.114.114
netsh interface ip add dns %NAME%  114.114.114.119
goto IP

:NO
goto restart

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