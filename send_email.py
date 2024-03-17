import smtplib, ssl

host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()

username = "pathiec92@gmail.com"
passkey = "yxictygrwuxvtgek"


def send_email(email, message):
    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, passkey)
        server.sendmail(from_addr=username, to_addrs=email, msg=message)
