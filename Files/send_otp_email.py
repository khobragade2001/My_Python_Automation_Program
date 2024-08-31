import random
import smtplib
import time

def otp_varification():
    otp = ''.join([str(random.randint(0,9)) for i in range(6)])
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('khobragade2001@gmail.com','zdgx hfvo hdjl umwp')
    msg = ('''Hello, This OTP send from Ashish for Demo purpose.\nYour OTP is : '''+str(otp))
    to_mail = input("Enter Your Email address : ")
    server.sendmail('khobragade2001@gmail.com', to_mail, msg)
    time.sleep(2)
    server.quit()
    return otp


otp = otp_varification()
varification = input("Enter OTP which is Receive on your email : ")
if otp == varification:
    print("OTP Successfully Verified")
else:
    print("You are entered Wrong OTP...............")