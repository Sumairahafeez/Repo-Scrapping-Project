from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time as sleep
import Innerscrappin2
import InnerScrapping
service = Service(executable_path="F:\\3rd Sem\\DSA Lab\\Week 3\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
# driver = webdriver.Chrome(executable_path='C:/Program Files/chromedriver-win64/chromedriver.exe')
Name = []
Description = []
Language = []
Stars = []
LastUpdated = []
minPage = 10
maxPage = 14
difference = maxPage-minPage
if difference <=4:
    for i in range(minPage,maxPage):
        driver.get(f'https://github.com/search?q=web+dev&type=repositories&p={i}')

        content = driver.page_source

        soup = BeautifulSoup(content, features="html.parser")
        # print(soup)
        for a in soup.findAll("div", attrs={"class": "flszRz"}):
            print(a)
            RepoName = a.find("a",attrs = {"class":"dIlPa"})
            RepoDescription = a.find("span",attrs = {"class":"cWNlgR"})
            language = a.find("li",attrs = {"class":"iyzdzM"})
            StarsGained = a.find("span",attrs = {"class":"hWqAbU"})
            Update = a.find("div",attrs = {"class":"liVpTx"})
            if RepoName != None and RepoDescription != None and language != None and StarsGained != None and Update != None:
                Name.append(RepoName.text)
                Description.append(RepoDescription.text)
                Language.append(language.text)
                Stars.append(StarsGained.text)
                LastUpdated.append(Update.text)
            # if(len(Name)==3):
            #     break    
    df = pd.DataFrame({"Name": Name, "Description":Description,"Language":Language,"Stars Gained":Stars,"Last Updated":LastUpdated})
    df.to_csv("Github2.csv", encoding="utf-8",index=False,mode="w") 
    InnerScrapping.Scrap() 
    Data = pd.read_csv('Github2.csv')
    Data.to_csv('Github.csv',encoding='utf-8',mode='a',header=False,index=False)
else:
    print(f'Too Many Pages cannot retrieve soo much data')        