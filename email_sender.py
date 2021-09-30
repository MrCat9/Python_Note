# -*- coding: UTF-8 -*-
# 发送邮件
# 推荐使用 send_email2receiver_list


import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
from retrying import retry


# 第三方 SMTP 服务
DEFAULT_SENDER_DICT = {
    'mail_host': 'smtp.sina.com',  # 设置服务器
    'mail_user': 'sender@sina.com',  # 用户名
    # 'mail_pass': '****',  # 登录密码
    'mail_pass': '****',  # 口令  # 20210123发现新浪的smtp服务改用口令登录
}

RETRY_TIMES = 3


def my_retry_on_exception(exception):
    print(f'[ERROR][email_sender.my_retry_on_exception][msg: {str(exception)}]')
    return True


class MyEmailSender(object):
    def __init__(self, sender_dict=''):
        if not sender_dict:
            # 使用默认 sender_dict
            self.sender_dict = DEFAULT_SENDER_DICT

    def gen_message(self, receiver: str, subject: str, text: str, attachment_path_list: [str]) -> MIMEMultipart:
        # 邮件内容
        message = MIMEMultipart()

        message['From'] = Header(self.sender_dict['mail_user'])  # 发件邮箱
        message['To'] = Header(receiver)  # 收件邮箱

        message['Subject'] = Header(subject)  # 主题

        content = MIMEText(text, 'plain', 'utf-8')  # 正文
        message.attach(content)

        for _attachment_path in attachment_path_list:  # 附件
            attachment = MIMEApplication(open(_attachment_path, 'rb').read())
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.split(_attachment_path)[-1])
            message.attach(attachment)

        return message

    def send_email(self, receiver: str, subject: str, text: str, attachment_path_list: [str]):
        """
        给单个收件邮箱发送邮件
        :param receiver: 收件邮箱
        :param subject: 主题
        :param text: 正文
        :param attachment_path_list: 附件路径
        :return:
        """

        # send_email_success_flag = False  # 默认发送失败

        # 邮件内容
        print(f'[INFO][msg: gen message for {receiver} ...]')
        message = self.gen_message(
            receiver=receiver,
            subject=subject,
            text=text,
            attachment_path_list=attachment_path_list
        )
        print(f'[INFO][msg: gen message for {receiver} success.]')

        # 发送
        print(f'[INFO][msg: send email to {receiver} ...]')
        send_email_success_flag = self._send(
            receiver=receiver,
            message=message
        )
        print(f'[INFO][msg: send email to {receiver} success.]')

        return send_email_success_flag

    def send_email2receiver_list(self, receiver_list: [str], subject: str, text: str, attachment_path_list: [str]):
        """
        给收件邮箱列表发送邮件
        :param receiver_list: 收件邮箱 列表
        :param subject: 主题
        :param text: 正文
        :param attachment_path_list: 附件路径
        :return:
        """

        send_email_success_flag_dict = {_k: False for _k in receiver_list}  # 默认发送失败
        receiver_list_len = len(receiver_list)

        for i, receiver in enumerate(receiver_list):
            try:

                print(f'[INFO][msg: ({i + 1}/{receiver_list_len}) {receiver} ...]')

                send_email_success_flag = self.send_email(
                    receiver=receiver,
                    subject=subject,
                    text=text,
                    attachment_path_list=attachment_path_list
                )
                send_email_success_flag_dict[receiver] = send_email_success_flag

                print(f'[INFO][msg: {receiver} success.]')
                # print(f'[INFO][msg: ({i + 1}/{receiver_list_len}) {receiver} success.]')

            except Exception as e:
                send_email_success_flag_dict[receiver] = False
                print(f'[ERROR][email_sender.MyEmailSender.send_email2receiver_list][msg: {str(e)}]')

                print(f'[INFO][msg: {receiver} fail.]')
                # print(f'[INFO][msg: ({i + 1}/{receiver_list_len}) {receiver} fail.]')

        return send_email_success_flag_dict

    @retry(stop_max_attempt_number=RETRY_TIMES, retry_on_exception=my_retry_on_exception,
           wait_random_min=3, wait_random_max=5)
    def _send(self, receiver: str, message: MIMEMultipart):
        # 发送
        # my_sender = smtplib.SMTP()  # 端口为25
        # my_sender.connect(MAIL_HOST, 25)  # 25 为 SMTP 非SSL加密连接端口号
        my_sender = smtplib.SMTP_SSL()  # 端口为465  # py36
        # my_sender = smtplib.SMTP_SSL(timeout=600)  # 端口为465  # py36
        # my_sender = smtplib.SMTP_SSL(host=self.sender_dict['mail_host'])  # 端口为465  # py37
        my_sender.connect(self.sender_dict['mail_host'], 465)  # 465有用SSL
        my_sender.login(self.sender_dict['mail_user'], self.sender_dict['mail_pass'])
        # my_sender.close()

        my_sender.sendmail(
            self.sender_dict['mail_user'],
            [receiver],
            message.as_string()
        )

        my_sender.close()

        return True


if __name__ == '__main__':
    # 测试数据
    test_receiver = 'receiver@qq.com'
    test_subject = 'this is subject from email_sender'
    test_text = 'this is text from email_sender'
    test_attachment_path_list = [
        'data/file1.csv',
        'data/file2.jpg',
        'data/file3.xls',
        'data/file4.pdf'
    ]

    # 发送邮件给单个邮箱
    mes = MyEmailSender()
    test_send_email_success_flag = mes.send_email(
        receiver=test_receiver,
        subject=test_subject,
        text=test_text,
        attachment_path_list=test_attachment_path_list
    )
    print(test_send_email_success_flag)

    # ----------------
    print('-' * 16)
    # ----------------

    # 测试数据
    test_receiver_list = [
        test_receiver,
        test_receiver,
        test_receiver,
        # '1001@xxxx.com',
        # '1002@xxxx.com',
        # '1003@xxxx.com',
    ]

    # 发送邮件给多个邮箱
    mes2 = MyEmailSender()
    test_send_email_success_flag_dict = mes2.send_email2receiver_list(
        receiver_list=test_receiver_list,
        subject=test_subject,
        text=test_text,
        attachment_path_list=test_attachment_path_list
    )
    print(test_send_email_success_flag_dict)
