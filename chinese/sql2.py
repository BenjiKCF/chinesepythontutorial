#coding:utf-8
import sqlite3


conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 執行查詢語句:
cursor.execute('select * from user where id=?', ('1',))
# 獲得查詢結果集:
values = cursor.fetchall()
print values

cursor.close()
conn.close()


    # SQL語句帶有參數
# cursor.execute('select * from user where name=? and pwd=?', ('abc', '123456'))
