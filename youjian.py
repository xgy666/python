import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

mail_host='smtp.qq.com'
#设置传输服务器（qq，163邮箱# ）
mail_user='XXX@qq.com'
mail_pass='twjxmfogqdiniegg'#激活码

sender='XXX@qq.com'  #发送者
receivers=['XXX@qq.com']  #接受者
f='fsdfdsf'
msg=MIMEMultipart()
html="""
<html>
<head></head>
<body>
<p>下面演示嵌入图片</p>
<section>
<img src='cid:0' style='float:left'/>
<img src='cid:1' style='float:left'/>
</setcion>
</body>
</html>
"""
#cid:0代表html中图片的位置表示方法

subject='您好！'
message=MIMEText('fdsfdsf','plain','utf-8')#class email.mime.text.MIMEText(_text[, _subtype[, _charset]])：MIME文本对象，其中_text是邮件内容，_subtype邮件类型，可以是text/plain（普通文本邮件），html/plain(html邮件), _charset编码，可以是gb2312等等。
#message=MIMEText(html,'html','utf-8'
msg['Subject']=Header(subject,'utf-8')
msg['From']=Header('我','utf-8')
msg['To']=Header('你','utf-8')
msg.attach(message)

#创建一个文本附件，这里是从指定文本中读取信息，然后创建一个文本信息
#att1=MIMEText('fdsfsdfsd','plain','utf-8')
att1=MIMEText(open('C:/Users/Administrator/result.txt','rb').read(),'plain','utf-8')
att1["Content-Type"] = 'application/octet-stream'  #指定类型
att1["Content-Disposition"] = 'attachment; filename="123.txt"'#这里的filename可以任意写，写什么名字，邮件中显示什么名字
msg.attach(att1)     #向其中添加附件

## 创建一个图片附件
img_path='C:/00b6eeeb52640917519dd5273a7e6dac.jpg'  #图片路径  这里的/要注意方向（电脑里面是C:\00b6eeeb52640917519dd5273a7e6dac.jpg）
image=MIMEImage(open(img_path,'rb').read())     #创建一个图片附件
image.add_header('Content-ID','<0>')   #指定图片的编号,必须要写
image.add_header('Content-Disposition', 'attachment', filename='test.jpg')#filename图片的名称
image.add_header('X-Attachment-Id', '0')
msg.attach(image)    #添加附件

#构造压缩附件
att = MIMEText(open('C:/00b6eeeb52640917519dd5273a7e6dac.rar','rb').read(),'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attatchment;filename="Pictures.rar"'
msg.attach(att)

try:
    smtpobj=smtplib.SMTP_SSL(mail_host, 465)  #端口号smtplib.SMTP( [host [, port [, local_hostname[,timeout]]]]) host是SMTP主机的服务器，其中163邮箱的是smtp.163.com,其他的可以在网上找到，port是端口号，这里默认的是25，local_hostname是你主机的SMTP,如果SMTP在你的本机上，你只需要指定服务器地址为 localhost 即可。timeout是设置的连接的限制时间，如果超过这个时间还没有连接上那么就会出现错误
    smtpobj.set_debuglevel(1)  #设置是否为调试模式。默认为False，即非调试模式，表示不输出任何调试信息。如果设置为1就表示输出调试信息
#    smtpobj.connect(mail_host,'25')   #SMTP.connect([host[, port]])连接到指定的smtp服务器。参数分别表示smpt主机和端口。注意: 也可以在host参数中指定端口号（如：smpt.yeah.net:25），这样就没必要给出port参数。
    smtpobj.login(mail_user,mail_pass)   #登录服务器，这里的user是邮箱的用户名，但是这里的password并不是你邮箱的密码，当你开启SMTP的时候会提示你设置一个密码，这里的密码就是对应的密码
    smtpobj.sendmail(sender,receivers,msg.as_string())   #SMTP.sendmail(from_addr, [to_addrs,], msg[, mail_options, rcpt_options]) 发送邮件，from_addr是发送方也就是你的邮箱地址，to_addr是接受方的地址，当然这里的可以填上多个邮箱账号发送给多个账号，如果有多个账号需要使用列表传递参数
    #SMTP.quit()断开连接
    print('发送成功')
except smtplib.SMTPException:
    print('发送失败')

