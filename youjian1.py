import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host='smtp.qq.com'         #设置传输服务器（qq，163邮箱# ）

mail_user='xxx@qq.com'             #qq邮箱号
mail_pass='twjxmfogqdiniegg'       #激活码

sender='xxx@qq.com'               #发送者
receivers=['xxx@qq.com','xxx@qq.com']              #接受者
f= 'chasijc'                    #发送的文本
                   
message=MIMEText(f,'plain','utf-8')       #第一个文本信息，第二个文本格式，第三个编码
#message['Content-Type'] = 'Text/HTML'
message['From']=Header('xgy','utf-8')     #发送人
message['To']=Header('guang','utf-8')     #收件人
subject='定时发送'
message['Subject']=Header(subject,'utf-8')   #发送邮件的标题
try:
    smtpobj=smtplib.SMTP_SSL(mail_host, 465)  #端口号
    smtpobj.set_debuglevel(1)
#    smtpobj.connect(mail_host,'25')
    smtpobj.login(mail_user,mail_pass)   #登录
    smtpobj.sendmail(sender,receivers,message.as_string())   #发送
    print('发送成功')
except smtplib.SMTPException:
    print('发送失败')

