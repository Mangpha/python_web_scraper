from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv
import os


class JobData:
    def __init__(self, data):
        self.title = data["title"]
        self.company = data["company"]
        self.location = data["location"]
        self.reward = data["reward"]
        self.link = data["link"]

    def __str__(self):
        return f"{self.title} / {self.company}"


class SearchAndCreateData:
    def __init__(self, keyword):
        self.keyword = keyword

    def Search(self):
        origin = "https://www.wanted.co.kr"
        searchData = []
        p = sync_playwright().start()

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.wanted.co.kr/search?query={self.keyword}&tab=position")

        for i in range(3):
            page.keyboard.down("End")
            time.sleep(2)

        soup = BeautifulSoup(page.content(), "html.parser")
        p.stop()
        jobs = soup.find_all("div", class_="JobCard_container__FqChn")
        for job in jobs:
            data = {
                "link": origin + job.find("a")["href"],
                "title": job.find("strong", class_="JobCard_title__ddkwM").text,
                "company": job.find("span", class_="JobCard_companyName__vZMqJ").text,
                "location": job.find("span", class_="JobCard_location__2EOr5").text,
                "reward": job.find("span", class_="JobCard_reward__sdyHn").text,
            }
            searchData.append(JobData(data))

        return searchData

    def CreateCSV(self, DB):
        filename = f"./jobs/{self.keyword}.csv"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            writter = csv.writer(f)
            writter.writerow(["Title", "Company", "Location", "Reward", "Link"])
            for i in range(len(DB)):
                writter.writerow(DB[i].__dict__.values())
