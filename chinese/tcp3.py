#coding:utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立連接:
s.connect(('127.0.0.1', 9999))
# 接收歡迎消息:
print s.recv(1024)
for data in ['Michael', 'Tracy', 'Sarah']:
    # 發送數據:
    s.send(data)
    print s.recv(1024)
s.send('exit')
s.close()
