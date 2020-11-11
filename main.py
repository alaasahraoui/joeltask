
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import datetime
import random
import pandas as pd
import os
from time import sleep
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
driver =webdriver.Chrome('chromedriver',chrome_options=chrome_options)

questions=[]
body=[]
df = pd.DataFrame(columns =['question','body'])


#set your number of pages here
for i in range(1,7):
  print('scraped page :'+str(i))
  driver.get("https://www.homeworkminutes.com/questions/view/"+str(i))
  for h1 in driver.find_elements_by_xpath('//h1[@class=\'post-title\']'):
    questions.append(h1.text)
  for h1_body in driver.find_elements_by_xpath('//div[@itemprop="description"]'):
    body.append(str(h1_body.text))
my_dataframe = pd.DataFrame({'Question' :questions,'Question_body' :body},) 

                                
my_dataframe.to_csv("questions.csv")
os.system("git add .")
os.system("git commit")

driver.quit()
