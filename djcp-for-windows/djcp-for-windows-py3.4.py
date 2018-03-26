# -*- coding: utf-8 -*-
import time
import wmi
import winreg
#py2.7
#import winreg
import sys
import webbrowser

def getTimeNow():
    #out_putfilename
    time_format='%Y_%m_%d_%H_%M_%S'
    time_now=time.strftime(time_format,time.localtime())
    return time_now
#output_filename=getTimeNow()+u"-Software-Install-List.html"

output_filename=input("输入报告名称(可指定磁盘，例如“d:主机报告”):")
fp=open(output_filename+".html","w",encoding="utf-8")

html_table_start_str='''<!DOCTYPE html>
<html>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
<head>
    <title>Software-Install-List</title>
<style>

body {
    width: 1024px;
    margin: 40px auto;
    font-family: 'trebuchet MS', 'Lucida sans', Arial;
    font-size: 14px;
    color: #444;
}

table {
    *border-collapse: collapse; /* IE7 and lower */
    border-spacing: 0;
    width: 100%;    
}

.bordered {
    border: solid #ccc 1px;
    -moz-border-radius: 6px;
    -webkit-border-radius: 6px;
    border-radius: 6px;
    -webkit-box-shadow: 0 1px 1px #ccc; 
    -moz-box-shadow: 0 1px 1px #ccc; 
    box-shadow: 0 1px 1px #ccc;         
}

.bordered tr:hover {
    background: #fbf8e9;
    -o-transition: all 0.1s ease-in-out;
    -webkit-transition: all 0.1s ease-in-out;
    -moz-transition: all 0.1s ease-in-out;
    -ms-transition: all 0.1s ease-in-out;
    transition: all 0.1s ease-in-out;     
}    
    
.bordered td, .bordered th {
    border-left: 1px solid #ccc;
    border-top: 1px solid #ccc;
    padding: 10px;
    text-align: left;    
}

.bordered th {
    background-color: #dce9f9;
    background-image: -webkit-gradient(linear, left top, left bottom, from(#ebf3fc), to(#dce9f9));
    background-image: -webkit-linear-gradient(top, #ebf3fc, #dce9f9);
    background-image:    -moz-linear-gradient(top, #ebf3fc, #dce9f9);
    background-image:     -ms-linear-gradient(top, #ebf3fc, #dce9f9);
    background-image:      -o-linear-gradient(top, #ebf3fc, #dce9f9);
    background-image:         linear-gradient(top, #ebf3fc, #dce9f9);
    -webkit-box-shadow: 0 1px 0 rgba(255,255,255,.8) inset; 
    -moz-box-shadow:0 1px 0 rgba(255,255,255,.8) inset;  
    box-shadow: 0 1px 0 rgba(255,255,255,.8) inset;        
    border-top: none;
    text-shadow: 0 1px 0 rgba(255,255,255,.5); 
}

.bordered td:first-child, .bordered th:first-child {
    border-left: none;
}

.bordered th:first-child {
    -moz-border-radius: 6px 0 0 0;
    -webkit-border-radius: 6px 0 0 0;
    border-radius: 6px 0 0 0;
}

.bordered th:last-child {
    -moz-border-radius: 0 6px 0 0;
    -webkit-border-radius: 0 6px 0 0;
    border-radius: 0 6px 0 0;
}

.bordered th:only-child{
    -moz-border-radius: 6px 6px 0 0;
    -webkit-border-radius: 6px 6px 0 0;
    border-radius: 6px 6px 0 0;
}

.bordered tr:last-child td:first-child {
    -moz-border-radius: 0 0 0 6px;
    -webkit-border-radius: 0 0 0 6px;
    border-radius: 0 0 0 6px;
}

.bordered tr:last-child td:last-child {
    -moz-border-radius: 0 0 6px 0;
    -webkit-border-radius: 0 0 6px 0;
    border-radius: 0 0 6px 0;
}



/*----------------------*/

.zebra td, .zebra th {
    padding: 10px;
    border-bottom: 1px solid #f2f2f2;    
}

.zebra tbody tr:nth-child(even) {
    background: #f5f5f5;
    -webkit-box-shadow: 0 1px 0 rgba(255,255,255,.8) inset; 
    -moz-box-shadow:0 1px 0 rgba(255,255,255,.8) inset;  
    box-shadow: 0 1px 0 rgba(255,255,255,.8) inset;        
}

.zebra th {
    text-align: left;
    text-shadow: 0 1px 0 rgba(255,255,255,.5); 
    border-bottom: 1px solid #ccc;
    background-color: #eee;
    background-image: -webkit-gradient(linear, left top, left bottom, from(#f5f5f5), to(#eee));
    background-image: -webkit-linear-gradient(top, #f5f5f5, #eee);
    background-image:    -moz-linear-gradient(top, #f5f5f5, #eee);
    background-image:     -ms-linear-gradient(top, #f5f5f5, #eee);
    background-image:      -o-linear-gradient(top, #f5f5f5, #eee); 
    background-image:         linear-gradient(top, #f5f5f5, #eee);
}

.zebra th:first-child {
    -moz-border-radius: 6px 0 0 0;
    -webkit-border-radius: 6px 0 0 0;
    border-radius: 6px 0 0 0;  
}

.zebra th:last-child {
    -moz-border-radius: 0 6px 0 0;
    -webkit-border-radius: 0 6px 0 0;
    border-radius: 0 6px 0 0;
}

.zebra th:only-child{
    -moz-border-radius: 6px 6px 0 0;
    -webkit-border-radius: 6px 6px 0 0;
    border-radius: 6px 6px 0 0;
}

.zebra tfoot td {
    border-bottom: 0;
    border-top: 1px solid #fff;
    background-color: #f1f1f1;  
}

.zebra tfoot td:first-child {
    -moz-border-radius: 0 0 0 6px;
    -webkit-border-radius: 0 0 0 6px;
    border-radius: 0 0 0 6px;
}

.zebra tfoot td:last-child {
    -moz-border-radius: 0 0 6px 0;
    -webkit-border-radius: 0 0 6px 0;
    border-radius: 0 0 6px 0;
}

.zebra tfoot td:only-child{
    -moz-border-radius: 0 0 6px 6px;
    -webkit-border-radius: 0 0 6px 6px
    border-radius: 0 0 6px 6px
}

</style>
</head>

<body>
<h1>自动测评工具 cptools v1.0 for windows  by chuanwei<br />(Test in Window7 32bit ):
</h1>
'''
html_table_header_str_system_info='''
<h1>系统基本信息:</h1>
<table class="bordered">
    <tr>
        <th>#</th>        
        <th>系统版本</th>
        <th>系统架构</th>
    </tr>
'''
html_table_end_str_system_info='''    
</table>
'''
html_table_header_str_software_list='''
<h1>系统安装的软件:</h1>
<table class="bordered">
    <tr>
        <th>#</th>        
        <th>Software</th>
        <th>Location</th>
    </tr>
'''
html_tr_left_str='''
<tr>
    <td>'''
html_tr_right_str='''
    </td>
</tr>
'''
html_table_end_str='''
</table>
</body>
</html>
'''
html_table_software_list=""

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_ALL_ACCESS)
for i in range(0, winreg.QueryInfoKey(key)[0]-1):
    try:
         key_name_under_uninstall=winreg.EnumKey(key, i)
         #print  key_name_under_uninstall
         each_key_path=r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"+'\\'+ key_name_under_uninstall
         #print each_key_path
         each_key= winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,each_key_path,0, winreg.KEY_ALL_ACCESS)
         try:
             softer_ware_name,typeresult= winreg.QueryValueEx(each_key,"DisplayName")
             #softer_ware_name=softer_ware_name.encode("UTF8").decode("UTF8")

             try:     
                 InstallLocation_name,typeresult= winreg.QueryValueEx(each_key,"InstallLocation")
                 #InstallLocation_name = InstallLocation_name.encode("UTF8").decode("UTF8")
                 if InstallLocation_name=="":
                     InstallLocation_name="NULL"
             except WindowsError:
                 InstallLocation_name="NULL"
             html_table_software_list = html_table_software_list + html_tr_left_str + str(i+1) + '''</td>
    <td>''' + softer_ware_name + '''</td>
    <td>''' + InstallLocation_name + html_tr_right_str
         except WindowsError:
             pass
    except WindowsError:
        pass
c = wmi.WMI ()
for sys in c.Win32_OperatingSystem():
    #print "Version:%s" % sys.Caption.encode("UTF8"),"Vernum:%s" % sys.BuildNumber
    #print  sys.OSArchitecture.encode("UTF8")#系统是32位还是64位的
    #print sys.NumberOfProcesses #当前系统运行的进程总数 for sys in c.Win32_OperatingSystem():
    
    html_table_system_info = html_tr_left_str + "1" +'''</td>
    <td>''' + sys.Caption + '''</td>
    <td>''' + sys.OSArchitecture + html_tr_right_str
    
    #html_output_system_info=html_table_start_str + html_table_header_str_system_info + sys.Caption.encode("UTF8") + html_table_end_str
    html_output_header=html_table_start_str #头部
    html_output_footer=html_table_end_str #底部
    html_output_system_info=html_table_header_str_system_info + html_table_system_info + html_table_end_str_system_info #系统信息
    html_output_software_list=html_table_header_str_software_list + html_table_software_list #软件列表
    

fp.write(html_output_header)

fp.write(html_output_system_info)
fp.write(html_output_software_list)

fp.write(html_output_footer)
fp.close()
