import smtplib
import ssl
import os

def send_email(message):
    global host, port, username, password
    host = "smtp.gmail.com"
    port = 465
    username = "tpradivgnanaraj@gmail.com"
    password = os.getenv("PASSWORDNEWSAPI")

    receiver = "tpradivgnanaraj@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
