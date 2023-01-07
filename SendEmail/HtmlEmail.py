from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

# create email

my_email = EmailMessage()

# create Template

html_templates = Template(Path("templates/index.html").read_text())
html_content = html_templates.substitute({'name': 'Sergey', 'date': 'tomorrow'})

my_email['from'] = 'Sergey' # message sender
my_email['to'] = 'friend@gmail.com'
my_email['subject'] = "Let's go out"  # theme
my_email.set_content(html_content, 'html')  # content

# send email with smtplib
with smtplib.SMTP(host='localhost', port=2525) as smtp_servser:
    smtp_servser.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_servser.send_message(my_email)
    print('Email was sent!') # Email was sent!
