# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = 'kachun1017@hotmail.com'
password = 'Zz37694917'
to_addr = 'kachun1017@gmail.com, andy.chan0214@gmail.com'
smtp_server = 'smtp.live.com'

msg = MIMEText('Please short stock x and long stock y ASAP! Arbitrage profit: _____ ', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Ben Fung <%s>' % from_addr)
msg['To'] = _format_addr(u'管理員 <%s>' % to_addr)
msg['Subject'] = Header(u'來自SMTP的Short Long signal……, Please short stock x and long stock y ASAP', 'utf-8').encode()

def sendmail(msg):
    server = smtplib.SMTP(smtp_server, 587)
    server.ehlo()
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
