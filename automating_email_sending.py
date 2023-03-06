# Automating email sending
# Ínstalling necessary libraries

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Writng the automation script

sender_email = 'your_email@gmail.com'
sender_password = 'email password'
recipients = ['your_email@gmail.com', 'your email password']
subject = 'Test email'
body = 'This is a test email'

# Message to send 

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = ', '.join(recipients)
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

# Server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, sender_password)
server.sendmail(sender_email, recipients, message.as_string())
server.quit()

# This is script will send an email with the subject "Test email" 
# and the body "This is a test email" to the recipients listed in 
# the recipients variable