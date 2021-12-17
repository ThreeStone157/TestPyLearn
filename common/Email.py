import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class Email:
    def send_email(self, file_path):
        # 第一步： 连接到smtp服务器
        smtp = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtp.login("邮箱", "秘钥")
        # 第二步：构建邮件
        smg = MIMEMultipart()
        text_smg = MIMEText("第一次测试一下邮件自动发送文本", "plain", "utf8")
        smg.attach(text_smg)

        # 添加附件
        file_msg = MIMEApplication(open(file_path, "rb").read())
        file_msg.add_header('content-disposition', 'attachment', filename='report.html')
        smg.attach(file_msg)

        smg["Subject"] = "Test1测试报告" # 主题
        smg["From"] = "XXX@qq.com" # 邮件内显示的发件人
        smg["To"] = "XX@163.com" # 邮件内显示的收件人

        # 第三步发送邮件
        smtp.send_message(smg, from_addr="XX@qq.com", to_addrs="XX@163.com")

if __name__ == "__main__":
    email = Email()
    email.send_email(r"F:\code\TestDevLearn\testcase\report.html")