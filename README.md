# Email-Notification
 
I have been meaning to buy the Philips 4K UHD monitor. The price is currently set to $479.99, but I want to wait until the price drops to $400. It is a tedious task to monitor the price every day. As a workaround, I wrote a Python program that essentially checks every hour, if the price dropped to $400. If the price does end up dropping to $400, an email will be sent out to notify me.
 
There are a few Python modules I leveraged. Two of which are 'requests' and 'BeautifulSoup.' The requests module allows us to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc). The HTML part of the response is parsed using the BeautifulSoup4 module. After it is parsed, we have the ability to scrape any specific information we would want, in our case, it is the price. On using the Google Chrome Developer Tool, I was able to see exactly which HTML tag has the price. It was a span tag. Using BeautifulSoup, I managed to scrape the price by referencing the id from the span tag.
 
In order to send an email, I had to enable a two-step verification using a less secure app (LSA) that connects to Google accounts using only the username and password verification for access and not OAuth. Here is the URL: https://myaccount.google.com/lesssecureapps?pli=1. If we want to use our Gmail password, we can enable 2 step verification using an alternative path, here is the URL for that: https://www.google.com/landing/2step/.
After enabling two-step authentication, navigate to ‘App Passwords - Google Account’ inside which we can create a password for any specific thing, in our case it is for the email credentials. The password generated for me was: 'mset kakrro adiko.'
 
Python module ‘smtplib’ is imported which is a protocol involved with sending e-mail and routing e-mail between mail servers.
 
Last, but not least, I imported the 'date' module so that I can instruct my program to check the price each hour.
