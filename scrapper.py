import requests
from bs4 import BeautifulSoup

LIMIT = 50


def get_last_page(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find('div', {'class': 'pagination'})

    # print(pagination)

    links = pagination.find_all('a')
    pages = []
    for link in links[:-1]:
        # print(link.find('span', {'class': 'pn'}))
        pages.append(int(link.find('span').string))
    # pages = pages[:-1]
    max_page = pages[-1]
    return max_page


def extract_job(html):
    job_title = html.find("h2").string
    if html.find("a",{"class":'turnstileLink'})  is not None:
            company_anchor = html.find("a",{"class":'turnstileLink'})
            company = str(company_anchor.string)
    else:
        company = str(html.find('span',{'class':'companyName'}).string)
    company = company.strip()
    location = html.find('div',{'class':'companyLocation'}).string
    job_id = html["data-jk"]
    # print(job_id)
    return {'title': job_title,'company':company,'location':location,'link':f"https://www.indeed.com/viewjob?jk={job_id}&from=web&vjs=3"}

    

def extract_jobs(last_page,url):
    jobs = []
    for page in range(last_page):
        # print(f"&start={page*LIMIT}")
        print(f"Scrapping page Indeed: Page {page}")

        result = requests.get(f"{url}&start={page*LIMIT}")
    # print(result.status_code)
        soup = BeautifulSoup(result.text,'html.parser')
        results = soup.find_all('a',{'class':'tapItem'})
        for result in results:
           job = extract_job(result)
           jobs.append(job)
    return jobs


def get_jobs(word):
    url = f"https://www.indeed.com/jobs?q={word}&limit=${LIMIT}"
    last_pages = get_last_page(url)
    jobs = extract_jobs(last_pages, url)
    return jobs

    
    











