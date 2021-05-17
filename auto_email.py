import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

class AutoEmail():
    def __init__(self, username, password, smtp_server='smtp.163.com'):
        self.username = username
        self.password = password
        self.smtp_server = smtp_server
        self.server = smtplib.SMTP(self.smtp_server, 25)
        self.server.set_debuglevel(1)
        self.server.login(self.username, self.password)

    @staticmethod
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def send(self, receiver, msg):
        msg = MIMEText(msg, 'plain', 'utf-8')
        msg['From'] = self._format_addr(f"Auto Email <{self.username}>")
        msg['To'] = self._format_addr(f"Luckky <{receiver}>")
        msg['Subject'] = Header('Your program is finished', 'utf-8').encode()
        self.server.sendmail(self.username, [receiver], msg.as_string())
        self.server.quit()


