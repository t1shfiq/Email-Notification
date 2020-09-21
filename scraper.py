import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.ca/Computer-Monitors-328E1CA-Adaptive-Sync-Replacement/dp/B07VLJPZDR/ref=sr_1_6?dchild=1&keywords=4k+monitor&qid=1600659292&sr=8-6'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_outprice").get_text()

    converted_price = float(price[0:3])

    if(converted_price < 400):
        send_mail()

        print(converted_price)
        print(title)

    if(converted_price > 400):
        send_mail


def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login('ali.tashfiq4@gmail.com', 'msetkakrroadiko')

        subject ='Price fell down to $400'
        body = 'Check URL https://www.amazon.ca/Computer-Monitors-328E1CA-Adaptive-Sync-Replacement/dp/B07VLJPZDR/ref=sr_1_6?dchild=1&keywords=4k+monitor&qid=1600659292&sr=8-6'

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(

            'ali.tashfiq4@gmail.com',
            msg
        )
        print('Email Sent')

        server.quit()

