# coding:utf-8

import sqlite3

# 連接到SQLite數據庫
# 數據庫文件是test.db
# 如果文件不存在，會自動在當前目錄創建:
conn = sqlite3.connect('test.db')
# 創建一個Cursor:
cursor = conn.cursor()
# 執行一條SQL語句，創建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 繼續執行一條SQL語句，插入一條記錄:
cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# 通過rowcount獲得插入的行數:
cursor.rowcount

# 關閉Cursor:
cursor.close()
# 提交事務:
conn.commit()
# 關閉Connection:
conn.close()
