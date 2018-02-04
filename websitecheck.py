import requests
import smtplib
from config import username, password
URL = 'http://lafleur.tech'
try:
    s=requests.get(URL)
except requests.exceptions.RequestException:
    email = smtplib.SMTP("smtp.gmail.com",587)
    email.ehlo()
    email.starttls()
    email.login(username,password)
    msg = """From: Website Checker <websitecheck@lafleur.tech>
To: Patrick <patrick@lafleur.tech>
Subject: Website Check

The lafleur.tech website appears to be down.
"""
    email.sendmail("websitecheck@lafleur.tech","patrick@lafleur.tech",msg)