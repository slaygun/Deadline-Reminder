import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import deadline

# Email content
email = MIMEMultipart()
email['From'] = 'nabhraghav@gmailcom'
email['To'] = 'e21cseu0434@bennett.edu.in'
email['Subject'] = 'Deadline tomorrow'

#Retrieving the data from deadline.py
body = deadline.body

email.attach(MIMEText(body, 'plain'))

# Email server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'nabhraghav@gmail.com'
smtp_password = 'rpvonmgbppiqmute'

# Establish a secure connection to the email server and login
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)

# Send the email if there is any event and close the connection 
if body!="":
    server.sendmail(email['From'], email['To'], email.as_string())
    print('Email sent successfully!\n_____________')
    server.quit()
else:
    print("nothing to send :/")
    server.quit()


