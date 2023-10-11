import os
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def send(form):
    msg = MIMEMultipart()
    
    msg['From'] = form['fullName']
    msg['To'] = ''
    msg['Subject'] = "User message from equify"
    message = str(f"Name: {form['fullName']} \r\nEmail: {form['email']} \r\nphone: {form['phone']} \r\nCompany: {form['company_name']}\r\nMessage: {form['message']}")
    msg.attach(MIMEText(message, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('birddetector@gmail.com', 'nhewpvjmdrblrwqe')
    
    text = msg.as_string()
    server.sendmail('birddetector@gmail.com', 'm32jawad@gmail.com', text)
    server.quit()