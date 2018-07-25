#coding:utf-8
import unittest,time
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib, os,sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

#发送测试报告，需要配置你的邮箱地址
def send_mail(file_new):
    f = open(file_new, "rb")
    mail_body = f.read()
    f.close()
    sender = 'lky8139@163.com'
    receiver = "971109235@qq.com"
    msg = MIMEText(mail_body, "html", "utf-8")
    msg['Subject'] = Header("自动化测试报告", "utf-8")
    msg["From"] = sender
    msg["To"] = receiver
    smtp = smtplib.SMTP()
    smtp.connect("smtp.163.com")
    smtp.login(sender, "w123456")
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print("email has sent out!")

#查找测试报告目录，找到最新生成的测试报告文件
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key = lambda fn : os.path.getmtime(testreport+ "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    #print(file_new)
    return file_new


#指定测试用例为当前文件夹下的test_case目录
test_dir = r'F:\Workspace\selenium\paperless_project\mail\test_case'
#print(test_dir)
testreport = r'F:\Workspace\selenium\paperless_project\mail\report'

discover = unittest.defaultTestLoader.discover(test_dir, pattern="*_case.py")

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = testreport + '/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u"测试报告",
                            description=u"运行环境: window 7, Firefore")

    runner.run(discover)
    fp.close()

    new_report = new_report(testreport)
    send_mail(new_report)

