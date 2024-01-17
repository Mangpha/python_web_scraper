import requests
from bs4 import BeautifulSoup

all_jobs = []


def get_pages(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))


def scrape_page(url):
    print(f"Scraping {url}")
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    jobs = soup.find("section", class_="jobs").find_all("li")[:-1]
    for job in jobs:
        title = job.find("span", class_="title").text
        company, position, region = job.find_all("span", class_="company")
        link = job.find("div", class_="tooltip").next_sibling["href"]
        job_data = {
            "title": title,
            "company": company.text,
            "position": position.text,
            "region": region.text,
            "url": f"https://weworkremotely.com{link}",
        }
        all_jobs.append(job_data)


total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")


for i in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={i + 1}"
    scrape_page(url)

print(len(all_jobs))
