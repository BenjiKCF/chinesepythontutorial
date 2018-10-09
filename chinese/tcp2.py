#coding:utf-8
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 可以用0.0.0.0綁定到所有的網絡地址，還可以用127.0.0.1綁定到本機地址。
# 監聽端口:
s.bind(('127.0.0.1',9999))

#listen()方法開始監聽端口 指定等待連接的最大數量：
s.listen(5)
print 'Waiting for connection...'

# 永久循環來接受來自客戶端的連接，accept()會等待並返回一個客戶端的連接:
while True:
    # 接受一個新連接:
    sock, addr = s.accept()
    t = threading.Thread(target = tcplink, args=(sock,addr))
    t.start()

def tcplink(sock,addr):
    print 'Accept new connection from %s:%s...'%addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!'%data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr
