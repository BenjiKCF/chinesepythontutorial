#coding:utf-8
import socket

# AF_INET指定使用IPv4協議
# 如果要用更先進的IPv6，就指定為AF_INET6
# SOCK_STREAM指定使用面向流的TCP協議
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('www.sina.com.cn',80))

# 發送數據
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收數據
buffer = []
# while循環中反覆接收
while True:
    # 每次最多接收1k字節:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

# 關閉連接
s.close()

header, html = data.split('\r\n\r\n', 1)
print header

# 把接收的數據寫入文件
with open('sina.html', 'wb') as f:
    f.write(html)
# sina.html is located at python folder
