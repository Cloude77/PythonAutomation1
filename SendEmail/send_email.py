from email.message import EmailMessage
import smtplib

# create email

my_email = EmailMessage()

my_email['from'] = 'Sergey' # message sender
my_email['to'] = 'neftianik@inbox.ru'
my_email['subject'] = "Hello from Python" # theme
my_email.set_content("Hey! How are you doing?") # content

# send email with smtplib
with smtplib.SMTP(host='localhost', port=2525) as smtp_servser:
    smtp_servser.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_servser.send_message(my_email)
    print('Email was sent!') # Email was sent!
