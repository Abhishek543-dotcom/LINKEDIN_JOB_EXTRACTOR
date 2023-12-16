import csv
import requests
from bs4 import BeautifulSoup

file = open('linkedin-jobs.csv', 'a', newline='', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(['Title', 'Company', 'Location', 'Apply'])


def linkedin_scraper(webpage, page_number):
    next_page = webpage + str(page_number)
    print(str(next_page))

    response = requests.get(str(next_page), verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')

    jobs = soup.find_all('div',
                         class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')

    for job in jobs:
        job_title = job.find('h3', class_='base-search-card__title').text.strip().encode('utf-8').decode('utf-8')
        job_company = job.find('h4', class_='base-search-card__subtitle').text.strip().encode('utf-8').decode('utf-8')
        job_location = job.find('span', class_='job-search-card__location').text.strip().encode('utf-8').decode('utf-8')
        job_link = job.find('a', class_='base-card__full-link')['href'].encode('utf-8').decode('utf-8')
        job_link = f'<a href="{job_link}">Apply</a>'
        writer.writerow([job_title, job_company, job_location, job_link])

    print('Data updated')

    if page_number < 25:
        page_number = page_number + 25
        linkedin_scraper(webpage, page_number)
    else:
        file.close()
        print('File closed')


linkedin_scraper(
    'https://www.linkedin.com/jobs/search?keywords=Data%20Engineer&location=India&locationId=&geoId=102713980&f_TPR=r86400&f_E=2%2C3&position=1&pageNum=0',
    0)



with open("data_cleaning.py") as f:
    exec(f.read())