from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
import time as sleep

# webdriver can be downloaded from
# https://sites.google.com/chromium.org/driver/downloads/versionselection?authuser=0

service = Service(executable_path="F:\\3rd Sem\\DSA Lab\\Week 3\\chromedriver-win64\\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(executable_path='C:/Program Files/chromedriver-win64/chromedriver.exe')
Name = []
Description = []
Language = []
Stars = []
LastUpdated = []
profilePhoto = []
Topics = []


driver.get("https://github.com/search?q=webdev&type=repositories&p=2")

content = driver.page_source

soup = BeautifulSoup(content, features="html.parser")
# print(soup)
for a in soup.findAll("div", attrs={"class": "flszRz"}):
    print(a)
    RepoName = a.find("a",attrs = {"class":"dIlPa"})
    RepoDescription = a.find("span",attrs = {"class":"cWNlgR"})
    language = a.find("li",attrs = {"class":"iyzdzM"})
    StarsGained = a.find("span",attrs = {"class":"hWqAbU"})
    Update = a.find("span",attrs = {"class":"hWqAbU"})
    Profile = a.find("div",attrs = {"class":"eurdCD"})
    topics = a.find("a",attrs = {"class":"iRNOQH"})
    if RepoName != None and RepoDescription != None and language != None and StarsGained != None and Update != None and Topics != None :
        Name.append(RepoName.text)
        Description.append(RepoDescription.text)
        Language.append(language.text)
        Stars.append(StarsGained.text)
        LastUpdated.append(Update.text)
        profilePhoto.append(Profile.src)
        Topics.append(topics.text)
    # if len(Name) == 50:
    #     break

df = pd.DataFrame({"Name": Name, "Description":Description,"Language":Language,"Profile Photo":profilePhoto,"Stars Gained":Stars,"Last Updated":Update,"Topics":Topics})
df.to_csv("Github.csv", encoding="utf-8")