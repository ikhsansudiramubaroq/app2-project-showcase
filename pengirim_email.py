import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "ikhsansudiramubaroq2910@gmail.com"
password = "vuis lgyt cvao yetc"

receiver = "ikhsansudiramubaroq2910@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: tes 
Hi !
Ini Ikhsan sudira
"""

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)