from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
import time
# webdriver can be downloaded from
# https://sites.google.com/chromium.org/driver/downloads/versionselection?authuser=0
def Scrap():
    service = Service(executable_path="F:\\3rd Sem\\DSA Lab\\Week 3\\chromedriver-win64\\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    driver = webdriver.Chrome(service=service, options=options)
    Issues = []
    PullRequests = []
    Forks = []
    Data = pd.read_csv('Github2.csv')
    Names = Data["Name"].values.tolist()
    for i in Names:
        try:
            driver.get(f'https://github.com/{i}')
            time.sleep(1) 
            content = driver.page_source
            soup2 = BeautifulSoup(content, features="html.parser") 
            for a in soup2.findAll("ul", attrs={"class":"UnderlineNav-body"}):
                start_time = time.time()
                issuesCount = a.find("span",attrs = {"id":"issues-repo-tab-count"}) 
                PullRequestsCout = a.find("span",attrs = {"id":"pull-requests-repo-tab-count"})
                Issues.append(issuesCount.text) if issuesCount else Issues.append(0)
                PullRequests.append(PullRequestsCout.text) if PullRequestsCout else PullRequests.append(0)
            ForksCount = soup2.find("span",attrs={"id":"repo-network-counter"})
            if ForksCount != None:
                Forks.append(ForksCount.text)
            else:
                Forks.append(0)
        except TimeoutException:
            print(f"Timeout while accessing {i}, skipping...")
        except Exception as e:
            print(f'error scrapping {i}: {e}')       
        finally:
            endTime = time.time()
            totalTime = endTime-start_time
            print(f'{i} has taken {totalTime} ms to get data')
            time.sleep(1)   
    Data["Issues"] = Issues
    Data["Forks"] = Forks
    Data["Pull Requests"] = PullRequests
    Data.to_csv("Github2.csv",index=False)            