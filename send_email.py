import smtplib, ssl
import os

username = os.getenv("USER_NAME")
passkey = os.getenv("PASSWORD")

host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()



def send_email(email, message):
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, passkey)
        server.sendmail(from_addr=username, to_addrs=email, msg=message)
