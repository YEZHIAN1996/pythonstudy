# coding: utf-8

import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart  # 邮件附件
import schedule

mail_host = 'smtp.qq.com'
mail_user = '1948521244'
mail_pass = '7478771111'

sender = '1948521244@qq.com'
receivers = ['yezhian1996@icloud.com']

# message = MIMEText('这是一个测试邮件', 'plain', 'utf-8')
message = MIMEMultipart()
message['From'] = Header(sender)
message['Subject'] = Header('python脚本测试', 'utf-8')

attr = MIMEText(open('send.py', 'rb').read(), 'base64', 'utf-8')
attr['Content-Type'] = 'application/octet-stream'
attr['Content-Disposition'] = 'attachment;filename="send.py"'

message.attach(attr)
message.attach(MIMEText('<p>这是一个带附件的邮件</p>', 'html', 'utf-8'))
def send():
    try:
        smtpobj = smtplib.SMTP()
        smtpobj.connect(mail_host, 25)
        smtpobj.login(mail_user, mail_pass)
        smtpobj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException as e:
        print(e)

if __name__ == '__main__':
    schedule.every(10).seconds.do(send)

    while 1:
        schedule.run_pending()
        time.sleep(1)