from bs4 import BeautifulSoup
import requests

url = 'https://www.seek.co.nz/jobs/full-time?daterange=31&keywords=%22devops%20engineer%22&salaryrange=120000-999999&salarytype=annual&sortmode=KeywordRelevance'
request = requests.get(url).text
soup = BeautifulSoup(request, 'lxml')
jobs = soup.find_all('article')

for job in jobs:
    job_title = job.find('a', class_='_2S5REPk').text
    company = job.find('a', class_='_17sHMz8').text.upper()
    location = job.find('strong', class_='_7ZnNccT').span.a.text
    raw_job_link = job.find('span', class_='_3mgsa7- _2X_OUt_ _1WgeL1f _3VdCwhL _2Ryjovs').span.h1.a['href']

    split_raw_link = raw_job_link.split('?')
    job_link = 'https://www.seek.co.nz' + split_raw_link[0]

    try:
        salary = job.find('span', class_='_7ZnNccT').text
    except Exception as e:
        salary = 'No salary info provided'
    
    print(company)
    print(job_title)
    print(location)
    print(salary)
    print(job_link)
    print()
    print()

