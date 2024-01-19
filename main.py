from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv


class JobData:
    def __init__(self, data):
        self.title = data["title"]
        self.company = data["company"]
        self.location = data["location"]
        self.reward = data["reward"]
        self.link = data["link"]

    def __str__(self):
        return f"{self.title} / {self.company}"


origin = "https://www.wanted.co.kr"
jobs_db = []
p = sync_playwright().start()


browser = p.chromium.launch(headless=False)

page = browser.new_page()
page.goto("https://www.wanted.co.kr/search?query=python&tab=position")
# time.sleep(1)
# page.click("button.Aside_searchButton__Xhqq3")
# time.sleep(1)
# page.get_by_placeholder("검색어를 입력해 주세요.").fill("python")
# time.sleep(1)
# page.keyboard.down("Enter")
# time.sleep(1)
# page.click("a#search_tab_position")
# time.sleep(1)

for i in range(3):
    page.keyboard.down("End")
    time.sleep(2)

soup = BeautifulSoup(page.content(), "html.parser")
jobs = soup.find_all("div", class_="JobCard_container__FqChn")
for job in jobs:
    data = {
        "link": origin + job.find("a")["href"],
        "title": job.find("strong", class_="JobCard_title__ddkwM").text,
        "company": job.find("span", class_="JobCard_companyName__vZMqJ").text,
        "location": job.find("span", class_="JobCard_location__2EOr5").text,
        "reward": job.find("span", class_="JobCard_reward__sdyHn").text,
    }
    jobs_db.append(JobData(data))

for i in range(len(jobs_db)):
    print(jobs_db[i])
p.stop()

file = open("jobs.csv", "w")
writter = csv.writer(file)
writter.writerow(["Title", "Company", "Location", "Reward", "Link"])
for i in range(len(jobs_db)):
    writter.writerow(jobs_db[i].__dict__.values())
