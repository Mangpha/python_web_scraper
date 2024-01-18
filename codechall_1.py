from requests import get
from bs4 import BeautifulSoup


class JobData:
    def __init__(self, job):
        self.title = job["title"]
        self.company = job["company"]
        self.region = job["region"]
        self.url = job["url"]


class Search:
    def __init__(self, keywords):
        self.keywords = keywords
        self.data = self.scrape()

    def scrape(self):
        origin = "https://remoteok.com"
        all_job = []
        for i in range(len(self.keywords)):
            res = get(
                f"{origin}/remote-{keywords[i]}-jobs",
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0"
                },
            )
            if res.status_code != 200:
                print("Response Error")
                return
            soup = BeautifulSoup(res.content, "html.parser")
            jobs = soup.find("table", id="jobsboard").find_all("tr", class_="job")
            for j in range(len(jobs)):
                data = jobs[j].find("td", class_="company_and_position")
                job = {
                    "title": data.find("h2", itemprop="title").text.strip(),
                    "company": data.find("h3", itemprop="name").text.strip(),
                    "region": data.find("div", class_="location").text,
                    "url": f"{origin}{data.find('a', class_='preventLink').attrs['href']}",
                }
                all_job.append(JobData(job))
        return all_job


keywords = ("flutter", "python", "golang")

job_data = Search(keywords)
