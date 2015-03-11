import cx_Oracle

#建立和数据库系统的连接

conn = cx_Oracle.connect('asi1/asi1/10.6.183.159/avtest')

#获取操作游标

cursor = conn.cursor()

#执行SQL,创建一个表

cursor.execute('select * from airline');

while(1):
 
        rs=cursor.fetchone()
 
        if rs == None:break
 
        print rs

#关闭连接，释放资源

cursor.close()

#执行完成，打印提示信息

print 'Completed!' 