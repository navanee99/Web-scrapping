from bs4 import BeautifulSoup

import requests

import time

html_text=requests.get('https://www.freelancer.com/jobs/?keyword=software%20developer').text
soup=BeautifulSoup(html_text,'lxml')
jobs=soup.find_all('div',class_='JobSearchCard-item')

def find_jobs():
    for index,job in enumerate(jobs):
        job_name=job.find('a',class_='JobSearchCard-primary-heading-link').text
        job_info=job.find('div',class_='JobSearchCard-primary-heading')
        more_info=job_info.a['href']
        due_date=job.find('span',class_='JobSearchCard-primary-heading-days').text
        salary=job.find('div',class_='JobSearchCard-primary-price')
        skills=job.find_all('a',class_='JobSearchCard-primary-tagsLink')
        with open(f'posts1/{index}.txt','w') as f:
            f.write(f'Job Title:{job_name.strip()}\n')
            f.write(f'Remaining Days to Apply:{due_date.strip()}\n')
            f.write(f'More info:{more_info}\n')
            if salary:
                f.write(f'Salary:{salary.text.replace(" ","").replace("(AvgBid)","").strip()}\n')
            f.write(f'Required skills:')
            for skill in skills:
                skill_name=skill.text
                if skill_name is not None:
                    f.write(f'{skill_name.replace(" ",",")}')
        print(f'File Saved:{index}')
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)