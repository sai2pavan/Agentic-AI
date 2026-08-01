#in this file we will use email library

import smtplib
import random

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

frommail = 'loyola.pavan.74@gmail.com'
tomail = 'bestfriendpavan2003@gmail.com'
subject = "Your OTP (One Time Password) for Login"
otp = random.randint(100000,999999)
message = f"Your OTP for login is {otp}"

msg = MIMEMultipart()
msg['From'] = frommail
msg['To'] = tomail
msg['Subject'] = subject
msg.attach(MIMEText(message))

text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('loyola.pavan.74@gmail.com','hhvb zljw pelr asjb')
print('login successfull')
server.sendmail(frommail,tomail,text)
print("success")

check = int(input("Enter OTP:"))
if check  == otp:
    print("OTP valid")
else:
    print("Incorrect OTP")