import requests
from bs4 import BeautifulSoup
import smtplib
import time

#URL of the product we are interested in
URL = 'https://www.amazon.ca/Computer-Monitors-328E1CA-Adaptive-Sync-Replacement/dp/B07VLJPZDR/ref=sr_1_6?dchild=1&keywords=4k+monitor&qid=1600659292&sr=8-6'

# user agent gives us information about our browser
# got it via a google seach for 'user agent'
# placed the information into a dictionary
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}


def check_price():

    # data returned from the website is stored in 'page'
    page = requests.get(URL, headers=headers)

    # parses the html content returned by requests 
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_outprice").get_text()

    # converts value to float and only takes the first three digits
    # cannot compare number and string
    converted_price = float(price[0:3])

    if(converted_price < 400):
        send_mail()

        print(converted_price)
        print(title)

def send_mail():

        # establish connection between our server and gmail
        server = smtplib.SMTP('smtp.gmail.com', 587)

        # ehlo is a command sent by an email server to identify itself
        server.ehlo()

        # encrypts connection
        server.starttls()
        server.ehlo()

        # Password generated from 2 step auth
        server.login('ali.tashfiq4@gmail.com', 'mset kakrro adiko')

        subject = 'Price fell down to $400'
        body = 'Check URL https://www.amazon.ca/Computer-Monitors-328E1CA-Adaptive-Sync-Replacement/dp/B07VLJPZDR/ref=sr_1_6?dchild=1&keywords=4k+monitor&qid=1600659292&sr=8-6'

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(

            'ali.tashfiq4@gmail.com',
            msg
        )
        print('Email Sent')

        server.quit()

while(True):
    check_price()
    time.sleep(60)