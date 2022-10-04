import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'example@gmail.com'
email_password = 'write-password-here'
email_receiver = 'write-email-receiver-here'
subject = 'Test automation'
body = """
This is a very fun automation
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
