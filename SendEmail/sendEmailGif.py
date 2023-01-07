from email.message import EmailMessage
import smtplib
from string import Template
from pathlib import Path

# create email

my_email = EmailMessage()

# create Template

html_templates = Template(Path("templates/index.html").read_text())
html_content = html_templates.substitute({'name': 'Sergey', 'date': 'tomorrow'})

my_email['from'] = 'Sergey <sg@gmail.com>'  # message sender
my_email['to'] = 'friend@gmail.com'
my_email['subject'] = "Email with image"  # them
my_email.set_content(html_content, 'html')  # content

# send gif
with open('images/email.gif', 'rb') as img:
    # read images/email.gif
    image_date = img.read()  # read file
    my_email.add_attachment(image_date, maintype='image', subtype='gif', filename='email.gif') # add file


# send email with smtplib
with smtplib.SMTP(host='localhost', port=2525) as smtp_servser:
    smtp_servser.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_servser.send_message(my_email)
    print('Email was sent!')  # Email was sent!
