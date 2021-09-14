#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests, csv

url = requests.get('https://realpython.github.io/fake-jobs/').text
soup = BeautifulSoup(url, 'lxml')
jobs = soup.find_all('div', class_='column is-half')

csv_file = open('jobs.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['COMPANY', 'JOB TITLE', 'LOCATION'])

for job in jobs:
    try:
        company_name = job.find('h3', class_='subtitle is-6 company').text.upper()
        job_title = job.find('h2', class_='title is-5').text
        location = job.find('p', class_='location').text.strip()

        print(company_name)
        print(job_title)
        print(location)
        print()

        csv_writer.writerow([company_name, job_title, location])

    except Exception as e:
        print(str(e))

csv_file.close()

    



