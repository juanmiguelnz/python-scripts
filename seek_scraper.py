#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests, csv

url = 'https://www.seek.co.nz/jobs/full-time?daterange=31&keywords=%22devops%20engineer%22&salaryrange=120000-999999&salarytype=annual&sortmode=KeywordRelevance'
request = requests.get(url).text
soup = BeautifulSoup(request, 'lxml')
jobs = soup.find_all('article')

with open('jobs.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['JOB TITLE', 'COMPANY', 'LOCATION', 'SALARY', 'LINK'])
    
    for job in jobs: 
        job_title = job.find('a', class_='_2S5REPk').text
        company = job.find('a', class_='_17sHMz8').text.upper()
        location = job.find('strong', class_='_7ZnNccT').span.a.text
        raw_job_link = job.find('a', class_='_2S5REPk')['href']

        split_raw_link = raw_job_link.split('?')
        job_link = 'https://www.seek.co.nz' + split_raw_link[0]

        try:
            salary = job.find('span', class_='_7ZnNccT').text
        except Exception as e:
            salary = 'No salary info provided'

        csv_writer.writerow([job_title, company, location, salary, job_link])
    
    print('CSV file has been created successfully!')
