# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host = "smtp.163.com"
mail_user = "zhangtingxuan"
mail_pass = "ztx123456"

sender = 'zhangtingxuan@163.com'
receivers = '892339906@qq.com'

message = MIMEText('Python 发送邮件测试', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error:无法发送邮件")
