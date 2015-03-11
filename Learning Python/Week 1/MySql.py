#-*- coding: utf-8 -*-  
data = []
data.append(['学号','姓名','成绩'])

import MySQLdb

conn = MySQLdb.connect(host="172.26.4.184",user="root",passwd="123456",db="db_extraedu",charset="utf8",port=3306)

cur = conn.cursor()
sql = 'select employeeNo,emailAddr from user limit 20'
cur.execute(sql)
result = cur.fetchall()
for l in result:
    data.append(l)
for l in data:
    print l;
