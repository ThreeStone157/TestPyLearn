import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from common.mylogging import MyLogger
from common.read_yaml import ReadYaml


# 封装的QQ邮箱发送功能类
class Emails:
    parameter = ""

    def __init__(self):
        ry = ReadYaml(r"..\config\email.yml")
        self.parameter = ry.parameter

    def send_email(self, file_name):
        # 第一步： 连接到smtp服务器
        smtp = smtplib.SMTP_SSL("smtp.qq.com", "465")
        # print(smtp)
        smtp.login(self.parameter["QQ_email"], self.parameter["login_token"])
        # 第二步：构建邮件
        smg = MIMEMultipart()
        text_smg = MIMEText(self.parameter["text_smg"], "plain", "utf8")
        smg.attach(text_smg)

        # 添加附件:测试报告
        file_path = self.parameter["report_file_path"] + r"\{}".format(file_name)
        file_msg = MIMEApplication(open(file_path, "rb").read())
        file_msg.add_header('content-disposition', 'attachment', filename=file_name)
        smg.attach(file_msg)

        # 添加附件：日志
        file_name2 = file_name.split(".")[0]
        file_path2 = self.parameter["log_file_path"] + r"\{}.txt".format(file_name2)
        file_msg2 = MIMEApplication(open(file_path2, "rb").read())
        file_msg2.add_header('content-disposition', 'attachment', filename="{}.txt".format(file_name2))
        smg.attach(file_msg2)

        smg["Subject"] = self.parameter["subject"]  # 主题
        smg["From"] = self.parameter["QQ_email"]  # 邮件内显示的发件人
        smg["To"] = self.parameter["to_email"]  # 邮件内显示的收件人
        try:
            # 第三步发送邮件
            smtp.send_message(smg, from_addr=self.parameter["QQ_email"], to_addrs=self.parameter["to_email"])
        except Exception as e:
            logging.error("发送邮件失败，失败的原因是:{}".format(e))


if __name__ == "__main__":
    email = Emails()
    email.send_email(r"2022_06_28_11_27_27.html")
