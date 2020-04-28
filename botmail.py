"""
April 28, 2020
This file contains a function that sends an email
"""
from secrets import emailPW, jakeEmail
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_the_mail(msgTxt = " ", msgHTML = " ", receiverEmail = jakeEmail):
    #user params 
    sender_email = "bookfinderbot1@gmail.com"
    receiver_email = receiverEmail
    password = emailPW

    message = MIMEMultipart("alternative")
    message["Subject"] = "New Books From Your Favorite Authors!"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = msgTxt
    html = msgHTML

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
        sender_email, receiver_email, message.as_string()
        )

    print("Message sent to {0}".format(receiver_email))


if __name__ == "__main__":
    send_the_mail()
