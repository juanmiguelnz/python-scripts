# json data is from https://salaries.devops-jobs.net/

import json, csv

with open('salaries.json', 'r') as json_file:
    data = json.load(json_file)

    with open('pay.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(['JOB TITLE', 'COMPANY LOCATION', 'SALARY IN USD', 'SALARY', 'SALARY CURRENCY', 'EXPERIENCE', 'WORK YEAR', 'COMPANY SIZE'])
        
        for item in data:
            salary = [
                item['job_title'],
                item['company_location'],
                item['salary_in_usd'],
                item['salary'],
                item['salary_currency'],
                item['experience_level'],
                item['work_year'],
                item['company_size']
            ]

            csv_writer.writerow(salary)
            print(salary)