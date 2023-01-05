#!/usr/bin/env python
# coding: utf-8

# In[178]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib.request
from bs4 import BeautifulSoup
import re
import urllib.request as ur
import pandas as pd

# In[179]:

base_options = Options()
base_options.add_experimental_option("detach", True)
base_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=base_service, options=base_options)
# 가상의 크롬브라우저 실행

url = "https://map.kakao.com/"

driver.get(url)

time.sleep(1)
driver.find_element(By.CLASS_NAME, "tf_keyword").send_keys("제주도렌트카\n")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="info.searchHeader.message"]/div/div[2]/a').send_keys(Keys.ENTER)
time.sleep(1)


all_rent_page = []

soup1=BeautifulSoup(driver.page_source,'html.parser')
tags1 = soup1.find_all('li', {"class" : "PlaceItem clickArea"})
rent_company=re.compile('[<]a.*href[=]["](http.*[#]comment)["]\starget')
company_page=rent_company.findall(str(tags1))
for page_num in company_page:
    all_rent_page.append(page_num)

    time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="info.search.place.more"]').send_keys(Keys.ENTER)
time.sleep(1)
soup2=BeautifulSoup(driver.page_source,'html.parser')
tags2 = soup2.find_all('li', {"class" : "PlaceItem clickArea"})
rent_company=re.compile('[<]a.*href[=]["](http.*[#]comment)["]\starget')
company_page2=rent_company.findall(str(tags2))
for page_num2 in company_page2:
    all_rent_page.append(page_num2)

for search_page in range(3,6):
    page_xpath = '//*[@id="info.search.page.no'+str(search_page)+'"]'
    
    time.sleep(1)
    driver.find_element(By.XPATH, page_xpath).send_keys(Keys.ENTER)
    time.sleep(1)
    
    soup3=BeautifulSoup(driver.page_source,'html.parser') 
    tags3 = soup3.find_all('li', {"class" : "PlaceItem clickArea"})
    rent_company=re.compile('[<]a.*href[=]["](http.*[#]comment)["]\starget')
    company_page3=rent_company.findall(str(tags3))
    for page_num3 in company_page3:
        all_rent_page.append(page_num3)

driver.find_element(By.XPATH, '//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)
for search_page in range(1,6):
    page_xpath2 = '//*[@id="info.search.page.no'+str(search_page)+'"]'
    
    time.sleep(1)
    driver.find_element(By.XPATH, page_xpath2).send_keys(Keys.ENTER)
    time.sleep(1)
    
    soup4=BeautifulSoup(driver.page_source,'html.parser') 
    tags4 = soup4.find_all('li', {"class" : "PlaceItem clickArea"})
    rent_company=re.compile('[<]a.*href[=]["](http.*[#]comment)["]\starget')
    company_page4=rent_company.findall(str(tags4))
    for page_num4 in company_page4:
        all_rent_page.append(page_num4)

driver.find_element(By.XPATH, '//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)
for search_page in range(1,4):
    page_xpath3 = '//*[@id="info.search.page.no'+str(search_page)+'"]'
    
    time.sleep(1)
    driver.find_element(By.XPATH, page_xpath3).send_keys(Keys.ENTER)
    time.sleep(1)
    
    soup5=BeautifulSoup(driver.page_source,'html.parser') 
    tags5 = soup5.find_all('li', {"class" : "PlaceItem clickArea"})
    rent_company=re.compile('[<]a.*href[=]["](http.*[#]comment)["]\starget')
    company_page5=rent_company.findall(str(tags5))
    for page_num5 in company_page5:
        all_rent_page.append(page_num5)
        


# In[180]:


all_rent_page


# In[242]:


len(all_rent_page)


# In[243]:


all_rent_page[192]


# In[244]:


for com_num in range(len(all_rent_page)):
    url2 = all_rent_page[com_num]
    url2
    driver.get(url2)
    time.sleep(1)
    soup6=BeautifulSoup(driver.page_source,'html.parser')
    time.sleep(1)

    while True:
        # more_review = soup6.find(attrs = {'class' : 'link_more'}).text

        if  soup6.find(attrs = {'class' : 'link_more'}):                        #more_review != '후기 더보기':
            driver.find_element(By.XPATH, '//*[@id="mArticle"]/div[6]/div[2]/a/span[1]').click()
        else:
            break

    category2 = soup6.find(attrs = {'class' : 'txt_location'}).text
    all_review_data = []

    if '렌터카' in category2:

        tags6 = soup6.find_all('div', {"class" : "cont_evaluation"})
        com_name = soup6.find('h2', {"class" : "tit_location"}).text

        rent_name=re.compile('link_user.*#none["][>](.*)[<][/]a[>]\n')
        writer_name=rent_name.findall(str(tags6))

        rent_date=re.compile('time_write["][>]20(.*)[<][/]span[>]')
        rent_date2=rent_date.findall(str(tags6))

        rent_score=re.compile('style[=]["]width[:](.*)[%][;]["][>][<][/]span[>]')
        rent_score2=rent_score.findall(str(tags6))

        rent_coment=re.compile('<span>(.*)[<][/]span[>]')
        rent_coment2=rent_coment.findall(str(tags6))

        for num in range(0,len(writer_name)):
            row_reiew_data = []
            row_reiew_data.append(writer_name[num])
            row_reiew_data.append(rent_coment2[num])
            row_reiew_data.append('카카오맵')
            number_score = int(rent_score2[num])//20
            row_reiew_data.append(number_score)
            row_reiew_data.append(rent_date2[num])
            row_reiew_data.append(com_name)
            all_review_data.append(row_reiew_data)

    else:
        pass

all_review_data


# In[230]:


column_name = ['WRITER','CONTENT','TYPE','SCORE','CREATED_AT','RENTAL_CAR_ID']
df2 = pd.DataFrame(
    all_review_data, columns = [column_name])
df2


# In[231]:


df2.shape

driver.close()
# In[ ]:




