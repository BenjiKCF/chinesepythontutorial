#coding:utf-8

from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...','plain','utf-8')

# 輸入Email地址和口令:
from_addr = raw_input('From: ')
password = raw_input('Password: ')
# 輸入SMTP服務器地址:
smtp_server = raw_input('SMTP server:')
# 輸入收件人地址:
to_addr = raw_input('To: ') # 由於可以一次發給多個人，所以傳入一個listp

import smtplib
server = smtplib.SMTP(smtp_server, 25)# SMTP協議默認端口是25
server.set_debuglevel(1) # 打印出和SMTP服務器交互的所有信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
