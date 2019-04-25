import os
import platform
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

class yemail:
    '''邮箱类'''
    def __init__(self, mailaddr, password, smtp_server):
        name, addr = parseaddr(mailaddr)
        self.user = addr.split('@')[0]
        self.password = password
        self.smtp_server = smtp_server
        self.mailaddr = addr
        self.pid = os.getpid()
        self.name = name
        #print(self.user, self.mailaddr, self.name)

    def _content_to_mail(self, to, subject, content):
        mail = MIMEText(content, _subtype = 'plain', _charset = 'utf-8')
        mail['From'] = self.mailaddr
        #mail['From'] = formataddr((Header(self.name, 'utf-8').encode(), self.mailaddr))
        mail['Subject'] = subject
        mail['To'] = ";".join(to)

        return mail

    def _send_email(self, to, subject, content, ssl = False):
        mail = self._content_to_mail(to, subject, content)

        if ssl == False:
            server = smtplib.SMTP(self.smtp_server, port = smtplib.SMTP_PORT, timeout = 30)
            #server = smtplib.SMTP(self.smtp_server, timeout = 30)
        else:
            server = smtplib.SMTP_SSL(self.smtp_server, port = smtplib.SMTP_SSL_PORT, timeout = 30)
            #server = smtplib.SMTP_SSL(self.smtp_server, timeout = 30)

        server.login(self.user, self.password)
        server.set_debuglevel(1)
        server.sendmail(self.mailaddr, to, mail.as_string())
        server.quit()

    def send_mail(self, to, subject, content):
        self._send_email(to, subject, content, ssl = False)

    def send_mail_ssl(self, to, subject, content):
        self._send_email(to, subject, content, ssl = True)

class y163email(yemail):
    '''163邮箱'''
    def __init__(self):
        title_addr = 'chenyichong' + ' <reg4fun@163.com>'
        #print(title_addr)
        super(y163email, self).__init__(title_addr, 'good123', 'smtp.163.com')

class y_status_email(y163email):
    '''发送状态的邮箱'''
    def __init__(self, subject):
        super(y_status_email, self).__init__()
        #'cos90zero@hotmail.com'
        #'reg4game@sina.com', 
        self.to_list = ['automsg@my.com', 'autopick@163.com']
        self.subject = subject

    def send_msg(self, msg):
        self.send_mail_ssl(self.to_list, self.subject, msg)

def run_entry():
    #w2l.info("{0} run.".format(__name__))
    print("{0} run.".format(__name__))

    yemail = y_status_email('测试')
    yemail.send_msg('测试邮件模块，请忽略本邮件')

def module_entry():
    #w2l.info("{0} module run.".format(__name__))
    #print("{0} module run.".format(__name__))
    pass

if __name__ == "__main__":
    run_entry()
else:
    module_entry()