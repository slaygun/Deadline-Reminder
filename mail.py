import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import deadline

# Email content
email = MIMEMultipart()
email['From'] = 'sender@gmailcom'  #from which u will send the email (do 2-step auth and create app password in google account settings)
email['To'] = 'reciever@gmail.com' #where u will get the email
email['Subject'] = 'Deadline tomorrow'

#Retrieving the data from deadline.py
body = deadline.body

email.attach(MIMEText(body, 'plain'))

# Email server settings
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'sender@gmail.com'
smtp_password = 'app pass created in google settings'

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


