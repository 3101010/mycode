#-*- coding:utf-8 -*-

import pymysql
import sqlite3
# db = pymysql.connect("localhost","root","1q2w!Q@W","butian")
#
# cursor = db.cursor()

#cursor.execute("DROP TABLE IF EXISTS BUTIAN")

# sql = """create table butian (
#          id int(6) NOT NULL auto_increment,
#          company_id int(6),
#          company_name char(100),
#          industry int(3),
#          company_url char(100),
#          PRIMARY KEY (id)
#     )"""
# cursor.execute(sql)

# sql1 = "INSERT INTO butian(id,company_id, company_name, industry, company_url) VALUES (null, 1222,'北京',11,'http://11111.com/')"
# cursor.execute(sql1)
#
# db.close()


db1 = sqlite3.connect('butian.db')
cursor1 = db1.cursor()

cursor1.execute("DROP TABLE IF EXISTS BUTIAN")

sql = """create table butian (
         company_id int(6),
         company_name char(100),
         industry int(3),
         company_url char(100),
         PRIMARY KEY(company_id)
      )"""
cursor1.execute(sql)
db1.commit()
db1.close()
