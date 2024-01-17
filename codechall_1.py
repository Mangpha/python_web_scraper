from requests import get
from bs4 import BeautifulSoup


class JobData:
    def __init__(self, job):
        self.title = (job.title,)
        self.company = (job.company,)
        self.position = (job.position,)
        self.region = (job.region,)
        self.url = job.url


class Search:
    def __init__(self, keywords, url, data=[]):
        self.keywords = keywords
        self.url = url
        self.data = data

    def scrape(self):
        for i in range(len(self.keywords)):
            res = get(
                self.url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/110.0"
                },
            )
        print(res.status_code)


keywords = ("flutter", "python", "golang")
origin = "https://remoteok.com"
