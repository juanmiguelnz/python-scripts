#!/bin/bash python

from datetime import datetime
import requests, time, os, smtplib, random
from bs4 import BeautifulSoup

email_add = os.environ.get('EMAIL_ADD')
email_pwd = os.environ.get('EMAIL_PWD')

url = 'https://www.theplantproject.co.nz/collections/all-plants/products/hoya-obovata'

# Set date/time format
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

def header():
    # Send a request using a random header
    user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
    'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/15.0 Chrome/90.0.4430.210 Mobile Safari/537.36'
]
    user_agent = random.choice(user_agent_list)
    headers = {'User-Agent': user_agent}
    return headers

while True:
    website_status = requests.get(url, headers=header()).status_code
    if website_status == 200:
        try:
            response = requests.get(url, headers=header()).text
            soup = BeautifulSoup(response, 'lxml')
            check_product = soup.find('div', id='product-add')

            if check_product == None:
                print('Plant still not available')
                time.sleep(60)
                continue
            else:
                print(date_time, 'The website has been updated.')
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.ehlo()

                    smtp.login(email_add, email_pwd)

                    subject = 'The website has been updated.'
                    body = 'The Plant Project has updated a page.'
                    msg = f'Subject: {subject}\n\n{body}'

                    smtp.sendmail(email_add, 'maricarvdelacruz@gmail.com', msg)
                    time.sleep(120)
                    continue
        except Exception as e:
            print(str(e))
    else:
        print('The website is unreachable.')



