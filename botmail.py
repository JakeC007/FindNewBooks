"""
April 28, 2020
This file contains a function that sends an email
"""
from secrets import emailPW, jakeEmail

def send_the_mail(msg = " "):
    import smtplib, ssl

    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "bookfinderbot1@gmail.com"  # Enter your address
    receiver_email = jakeEmail  # Enter receiver address
    password = emailPW
    message = "Subject: New Books From Your Favorite Authors!\n\n" + msg

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    print("Message sent to {0}".format(receiver_email))


if __name__ == "__main__":
    send_the_mail()
