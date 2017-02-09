#! /usr/local/bin/python
import time

SMTPserver = 'smtp.mail.com'
sender = 'mail@sender.com'
# you can send multiple emails like ['mail1@example.com',mail2@example.com,'mail..etc']
destinations = ['mail@destination.com']

USERNAME = "mail@sender.com"
PASSWORD = "yourPassword"

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'

content = """\
Your Email Message here!
"""

subject = "Sending Email with Python 3.x"



from smtplib import SMTP_SSL as SMTP  
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText
# start to send emails
for destination in destinations:
    try:
        msg = MIMEText(content, text_subtype)
        msg['Subject'] = subject
        msg['From'] = sender  # some SMTP servers will do this automatically, not all

        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(USERNAME, PASSWORD)
        try:
            conn.sendmail(sender, destination, msg.as_string())
            #printing the email sended
            print("Sended to: ", destination)
        finally:
            conn.quit()
    except:
        print("Oops!")
    # a little pause before sending another one
    time.sleep(20)
