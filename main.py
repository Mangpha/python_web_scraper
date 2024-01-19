from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()
page.goto("https://www.wanted.co.kr/jobsfeed")
time.sleep(3)
page.click("button.Aside_searchButton__Xhqq3")
time.sleep(3)
page.get_by_placeholder("검색어를 입력해 주세요.").fill("python")
time.sleep(3)
page.keyboard.down("Enter")
time.sleep(3)
page.click("a#search_tab_position")
time.sleep(3)

for i in range(3):
    page.keyboard.down("End")
    time.sleep(3)

content = page.content
soup = BeautifulSoup(content, "html.parser")
p.stop()
