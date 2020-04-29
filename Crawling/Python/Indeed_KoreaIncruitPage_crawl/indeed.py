import requests
from bs4 import BeautifulSoup

URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=%EB%8D%B0%EC%9D%B4%ED%84%B0+%EB%A7%88%EC%BC%80%ED%8C%85&limit=50&radius=25"


def extract_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {
        'class': 'pagination'
    }).find_all("span", {'class': 'pn'})

    pages = []
    for page in pagination[:-1]:
        page = int(page.string)
        pages.append(page)
    return pages[-1]


def extract_job(html):
    title = html.find("div", {'class': 'title'}).find('a')['title']
    company = html.find("div", {'class': 'sjcl'})
    company_anchor = company.find('span').string
    if company:
        if company_anchor is None:
            company = "*회사없음*"
        else:
            company = company_anchor.strip().strip("\n")
    else:
        company is None
    location = html.find("div", {
        'class': 'sjcl'
    }).find('span', {
        'class': 'location'
    }).string
    job_link = html.find("div", {'class': 'title'}).find('a')['href']

    return {
        'title': title,
        'company': company,
        'location': location,
        'link': job_link
    }


def multi_req_page(last_page):
    jobs = []

    for page in range(last_page):
        print(f"Scrapping page : {page+1}")
        if page == 0:
            result = requests.get(f"{URL}&start={page*50}")
        else:
            result = requests.get(f"{URL}&start={page*50}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {'class': 'jobsearch-SerpJobCard'})
        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs
