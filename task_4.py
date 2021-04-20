import smtplib
from email.mime.text import MIMEText


def send_email(self, to_whom, message):
    you = to_whom
    login = 'al6938@ukr.net'
    passw = 'L1e6GTuj7aJgCY2g'
    url = 'smtp.ukr.net'
    msg = MIMEText(message)
    msg['Subject'] = 'currensy exchange '
    msg['From'] = login
    msg['To'] = 'omelchenkorv@gmail.com'

    server = smtplib.SMTP_SSL(url, 465)
    server.login(login, passw)
    server.sendmail(login, you, msg.as_string())
    return server.close()
