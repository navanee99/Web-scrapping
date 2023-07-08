from bs4 import BeautifulSoup

import requests
import time


def find_jobs():
    html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35').text
    soup=BeautifulSoup(html_text,'lxml')

    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
    for index,job in enumerate(jobs):
        published_date=job.find('span',class_='sim-posted').span.text
        if('today','few' in published_date):
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            more_info=job.header.h2.a['href']
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            with open(f'posts/{index}.txt','w') as f:
                    f.write(f"Company Name:{company_name.strip()} \n")
                    f.write(f"Required Skills:{skills.strip()} \n")
                    f.write(f"Publised Time:{published_date.strip()}\n")
                    f.write(f"More info:{more_info}")
            print(f'File Saved:{index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait*60)


