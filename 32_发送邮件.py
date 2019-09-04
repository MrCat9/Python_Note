# -*- coding: UTF-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
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

# 添加 excel 附件
excel_path = 'test_excel.xls'
excel_attachment = MIMEApplication(open(excel_path, 'rb').read())
excel_attachment.add_header('Content-Disposition', 'attachment', filename=excel_path)
message.attach(excel_attachment)

# 添加 log 附件
log_path = 'test_log.log'
log_attachment = MIMEApplication(open(log_path, 'rb').read())
log_attachment.add_header('Content-Disposition', 'attachment', filename=log_path)
message.attach(log_attachment)

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.close()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print("Error: 无法发送邮件")
    print(str(e))

