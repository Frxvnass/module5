import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()

def send_mail(sender : str,
       password:str,
        receiver:str,
         subject:str,
          body:str):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        server.login(sender,password)
        server.send_message(msg)
        print('Sent')

send_mail(
    sender=os.getenv('email_from'),
    password= os.getenv('app_password'),
    receiver=os.getenv('receiver'),
    subject="Hello,dear",
    body="Email yubormoq"
)