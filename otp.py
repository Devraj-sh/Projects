import random
import smtplib
from email.mime.text import MIMEText
from random import randint

def optgenerator():
    l = [[] for _ in range(4)]
    for i in range(4):
        l[i].append(random.randint(0, 9))

    s_email =input("Enter sender's email: ")
    passw = input("enter sender's Gmail code:")  # need to generate app password from  sender's gmail
    r_email = input("enter reciever's email:")
    sub = "OTP"
    text = l
    msg = f"Subject: {sub}\n\n{text}"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(s_email,passw)
    server.sendmail(s_email, r_email, msg)
    print("\u2714\u2714Your OTP has been sent successfully\u2714\u2714")

    l2 = [[] for _ in range(4)]
    c=0
    for i in range(4):
        l2[i].append(int(input("enter your {i+1} OTp number:")))
        if l[i]==l2[i]:
            c+=1
        else:
            print("\u274C\u274COTP numbers do not match\u274C\u274C")
    if c==4:
        print("\u2714\u2714Your entered OTP is correct\u2714\u2714")
optgenerator()
