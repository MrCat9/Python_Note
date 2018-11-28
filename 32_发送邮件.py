# -*- coding: UTF-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.sina.com"  # 设置服务器
mail_user = "111sina.com"  # 用户名
mail_pass = "···"  # 口令

sender = '111@sina.com'
receivers = ['222@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEMultipart()
message['From'] = Header("111@sina.com")
message['To'] = Header("222@qq.com")

subject = '我的主题...'
message['Subject'] = Header(subject)

content1 = MIMEText('我的正文。。。', 'plain', 'utf-8')
message.attach(content1)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
    print(str(e))

smtpObj.close()
