# Python Bot to check if an item is in stock from any online store. If it is, it sends a notification email to you.
from bs4 import BeautifulSoup
import requests
import smtplib, ssl

site = '' # The item page which you want to check
clas = '' # The element class of the 'In Stock' button or something (This should be gathered when it is out of stock)

password = '' # The password of the sender gmail account
sender = '' # The email address of the sender gmail account
receiver = '' # The receiver email account
name = '' # Name of recipient
context = ssl.create_default_context()
port = 465

def email():
    message = f"""From: Stock Checker <{sender}>
    To: {name} <{receiver}>
    Subject: Item In Stock

    Your item is in stock!

    Buy Here: {site}
    """
    print(message)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)

loop = True
while loop:
    page = requests.get(site).text
    soup = BeautifulSoup(page, 'html.parser')
    if soup.find(class_=clas) == None:
        print('In Stock!')
        email()
        loop = False
