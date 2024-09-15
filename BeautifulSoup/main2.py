from bs4 import BeautifulSoup
import time
import re

import requests

def parse_skills(input_string):
    
    input_string = input_string.strip().lower()
    
    input_string = re.sub(r'[,\s]+', ',', input_string)
    
    return [skill.strip() for skill in input_string.split(',') if skill.strip()]

familiar_skill_input = input('Enter the skills you are familiar with: ')

familiar_skill = parse_skills(familiar_skill_input)

print(f'Filtering out {familiar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=India&txtKeywords=python&txtLocation=India&cboWorkExp1=0').text

    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for job in jobs:
        published_date = soup.find('span', class_ = 'sim-posted').span.text

        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')

            skills_text = soup.find('span', class_ = 'srp-skills').text.lower()
            
            skills = parse_skills(skills_text)

            more_info = job.header.h2.a['href']

            if any(skill in skills for  skill in familiar_skill):
                print(f"Company Name: {company_name.strip()}\n")
                print(f"Required Skills: {', '.join(skills)}\n")
                print(f"More Info: {more_info}\n")

                print(' ')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 2
        print(f'Waiting for {time_wait} minutes')
        time.sleep(120)

