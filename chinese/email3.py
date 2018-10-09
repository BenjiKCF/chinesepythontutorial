#coding:utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header (name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = raw_input('SMTP server: ')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python愛好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理員 <%s>' % to_addr)
msg['Subject'] = Header(u'來自SMTP的問候……', 'utf-8').encode()

# 郵件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

# 添加附件就是加上一個MIMEBase，從本地讀取一個圖片:
with open('/Users/michael/Downloads/test.png', 'rb') as f:
    # 設置附件的MIME和文件名，這裡是png類型:
    mime = MIMEBase('image', 'png', filename='test.png')
    # 加上必要的頭信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的內容讀進來:
    mime.set_payload(f.read())
    # 用Base64編碼:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

# Gmail的SMTP端口是587
smtp_server = 'smtp.gmail.com'
smtp_port = 587
# SMTP服務必須要加密傳輸
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls() # 創建了安全連接
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
