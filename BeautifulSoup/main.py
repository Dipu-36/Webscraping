from bs4 import BeautifulSoup
import time

import requests

print('Put some skill that you are not familiar with: ')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=India&txtKeywords=python&txtLocation=India&cboWorkExp1=0').text

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for job in jobs:
        published_date = soup.find('span', class_ = 'sim-posted').span.text

        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')

            skills = soup.find('span', class_ = 'srp-skills').text.replace(' ','')

            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                print(f"Company Name: {company_name.strip()}")
                print(f"Required Skills: {skills.strip()}")
                print(f"More INfor: {more_info}")

                print(' ')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 2
        print(f'Waiting for {time_wait} minutes')
        time.sleep(120)

