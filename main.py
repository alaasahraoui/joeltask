
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import datetime
import random
import pandas as pd
import os
from time import sleep

import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import datetime
import random
import pandas as pd
import os
from time import sleep
import smtplib



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
for i in range(1,780000):
  print('scraped page :'+str(i))
  driver.get("https://www.homeworkminutes.com/questions/view/"+str(i))
  for h1 in driver.find_elements_by_xpath('//h1[@class=\'post-title\']'):
    questions.append(h1.text)
  for h1_body in driver.find_elements_by_xpath('//div[@itemprop="description"]'):
    body.append(str(h1_body.text))
my_dataframe = pd.DataFrame({'Question' :questions,'Question_body' :body},) 

                                
my_dataframe.to_csv("questions.csv")
os.system("git add .")
print('added')
os.system("git branch -M main")
print('branched')
os.system("git push -u origin main --force")
print('pushed')

driver.quit()
def send_an_email():
    toaddr = 'sahraoui.alaaeddine@gmail.com'    
    me = 'sahraoui.alaaeddine@gmail.com' 
    subject = "What's News"

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = me
    msg['To'] = toaddr
    msg.preamble = "test " 
    #msg.attach(MIMEText(text))

    part = MIMEBase('application', "octet-stream")
    part.set_payload(open("questions.csv", "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="questions.csv"')
    msg.attach(part)

    try:
       s = smtplib.SMTP('smtp.gmail.com', 587)
       s.ehlo()
       s.starttls()
       s.ehlo()
       s.login(user = 'sahraoui.alaaeddine@gmail.com', password = 'ksvablrpdktsqabt')
       #s.send_message(msg)
       s.sendmail(me, toaddr, msg.as_string())
       s.quit()
    #except:
    #   print ("Error: unable to send email")
    except SMTPException as error:
          print ("Error")

send_an_email()
