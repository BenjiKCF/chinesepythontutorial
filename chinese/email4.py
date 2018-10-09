#coding:utf-8

# part 1 receive email

import poplib
# 輸入郵件地址, 口令和POP3服務器地址:
email = raw_input('Email: ')
password = raw_input('Password: ')
pop3_server = raw_input('POP3 server: ')

# 連接到POP3服務器
server = poplib.pop3(pop3_server)
# 可以打開或關閉調試信息:
# server.set_debuglevel(1)
# 可選:打印POP3服務器的歡迎文字:
print(server.getwelcome())
# 身份認證:
server.user(email)
server.pass_(password)
# stat()返回郵件數量和佔用空間:
print('Messages: %s. Size: %s' % server.stat())
# list()返回所有郵件的編號:
resp, mails, octets = server.list()
# 可以查看返回的列表類似['1 82923', '2 2184', ...]
print mails
# 獲取最新一封郵件, 注意索引號從1開始:
index = len(mails)
resp, lines, octets = server.retr(index)
# retr()把每一封郵件內容拿到
# lines存儲了郵件的原始文本的每一行,
# 可以獲得整個郵件的原始文本:
msg_content = '\r\n'.join(lines)
# 稍後解析出郵件:
msg = Parser().parsestr(msg_content)
# 可以根據郵件索引號直接從服務器刪除郵件:
# server.dele(index)
# 關閉連接:
server.quit()

# part 2 parser
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

msg = Parser().parsetr(msg_content)

# indent用於縮進顯示:
def print_info(msg, indent=0):
    if indent == 0:
         # 郵件的From, To, Subject存在於根對象上:
         for header in ['From', 'To', 'Subject']:
             value = msg.get(header, '')
             if value:
                 if header == 'Subject':
                     #需要解碼Subject字符串:
                     value = decode_str(value)
                else:
                # 需要解碼Email地址:
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                value = u'%s <%s>' % (name, addr)
            print('%s%s: %s' % ('   '*indent, header, value))
    if (msg.is_multipart()):
        # 如果郵件對象是一個MIMEMultipart,
        # get_payload()返回list，包含所有的子對象:
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            print('%spart %s' % ('  ' * indent, n))
            print('%s--------------------' % ('  ' * indent))
            # 遞歸打印每一個子對象:
            print_info(part, indent + 1)
    else:
        # 郵件對象不是一個MIMEMultipart,
        # 就根據content_type判斷:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            # 純文本或HTML內容:
            content = msg.get_payload(decode=True)
            # 要檢測文本編碼:
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('  ' * indent, content + '...'))
        else:
            # 不是文本,作為附件處理:
            print('%sAttachment: %s' % ('  ' * indent, content_type))

def decode_str(s):
    value, charset = decode_header(s)[0]#decode_header()返回一個list，因為像Cc、Bcc這樣的字段可能包含多個郵件地址，所以解析出來的會有多個元素。
    if charset:
        value = value.decode(charset)
    return value

#需要檢測編碼，否則，非UTF-8編碼的郵件都無法正常顯示
def guess_charset(msg):
    # 先從msg對象獲取編碼:
    charset = msg.get_charset()
    if charset is None:
        # 如果獲取不到，再從Content-Type字段獲取:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
