from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import os

from selenium.webdriver.chrome.options import Options
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc
from datetime import datetime
import time
import pandas as pd
import numpy as np
import cx_Oracle
import re
from tqdm import tqdm
from IPython import display

import urllib

options = Options()
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
naver_driver = webdriver.Chrome(service=service, options=options)

naver_list = ['제주도%20제주아산렌트카']

star_lst = []
a_list = []
oper_list = []
nic_list = []
re_list = []
date_list = []
tag_list = []
re_star_list = []

for keyword in naver_list:
    print(f"이번에 찾을 키워드 : {keyword}")

    try:
        #         naver_map_url = f"https://map.naver.com/v5/search/{parse.quote(keyword)}"
        naver_map_url = f"https://map.naver.com/v5/search/{keyword}"
        #         naver_mqp_url = 'https://map.naver.com/v5/search/%EC%A0%9C%EC%A3%BC%EB%8F%84%20%EC%9D%B8%ED%84%B0%ED%8C%8C%ED%81%AC%EB%A0%8C%ED%8A%B8%EC%B9%B4/place/1058167611?c=14082020.2873345,3962314.0822643,15,0,0,0,dh&isCorrectAnswer=true'

        #         https://map.naver.com/v5/search/%EC%A0%9C%EC%A3%BC%EB%8F%84%20%EC%9D%B8%ED%84%B0%ED%8C%8C%ED%81%AC%EB%A0%8C%ED%8A%B8%EC%B9%B4/place/1058167611?c=14082020.2873345,3962314.0822643,15,0,0,0,dh&isCorrectAnswer=true

        naver_driver.get(naver_map_url)
        naver_driver.implicitly_wait(1)

        naver_driver.switch_to.frame('entryIframe')
        naver_driver.implicitly_wait(1)

        #         time.sleep(10)

        # 별점 수집
        try:
            naver_driver.find_element(By.CLASS_NAME, 'PXMot.LXIwF')
            naver_driver.implicitly_wait(1)
            star = naver_driver.find_element(By.CLASS_NAME, 'PXMot.LXIwF').text
            naver_driver.implicitly_wait(1)
            print(star)
            star_lst.append(star)

        except:
            print('별점없음')
            star_lst.append('')

        # 운영시간 수집
        try:
            naver_driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[6]/div/div[2]/div/ul/li[2]/div/a')
            naver_driver.implicitly_wait(1)
            naver_driver.find_element(By.XPATH,
                                      '//*[@id="app-root"]/div/div/div/div[6]/div/div[2]/div/ul/li[2]/div/a').click()
            naver_driver.implicitly_wait(1)
            oper = naver_driver.find_element(By.CLASS_NAME, 'kGc0c').text
            print(oper)
            naver_driver.implicitly_wait(1)
            oper_time = naver_driver.find_element(By.CLASS_NAME, 'qo7A2').text
            print(oper_time)
            oper_list.append(oper + ' ' + oper_time)

        except:
            print('운영시간없음')
            oper_list.append('')

        try:
            naver_driver.implicitly_wait(1)
            naver_driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a[2]')
            naver_driver.implicitly_wait(1)
            naver_driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a[2]').click()
            naver_driver.implicitly_wait(1)
            print('리뷰 클릭')

            try:
                # 스크롤 내리기 이동 전 위치
                scroll_location = naver_driver.execute_script("return document.body.scrollHeight")

                while True:
                    # 현재 스크롤의 가장 아래로 내림
                    naver_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                    # 전체 스크롤이 늘어날 때까지 대기
                    time.sleep(2)

                    # 늘어난 스크롤 높이
                    scroll_height = naver_driver.execute_script("return document.body.scrollHeight")

                    # 늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
                    if scroll_location == scroll_height:
                        break

                    # 같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
                    else:
                        # 스크롤 위치값을 수정
                        scroll_location = naver_driver.execute_script("return document.body.scrollHeight")

                    naver_driver.implicitly_wait(5)
                    # print('스크롤 내림')

            except:
                print('스크롤 안됨')

            # 더보기 클릭
            try:
                #                 naver_driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a[2]')
                naver_driver.find_element(By.CLASS_NAME, 'fvwqf')
                naver_driver.implicitly_wait(5)

                while True:
                    #                     naver_driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a[2]').click()
                    naver_driver.find_element(By.CLASS_NAME, 'fvwqf').click()
                    naver_driver.implicitly_wait(5)
                    # print('더보기 클릭')

                    try:
                        # 스크롤 내리기 이동 전 위치
                        scroll_location = naver_driver.execute_script("return document.body.scrollHeight")

                        while True:
                            # 현재 스크롤의 가장 아래로 내림
                            naver_driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                            # 전체 스크롤이 늘어날 때까지 대기
                            time.sleep(2)

                            # 늘어난 스크롤 높이
                            scroll_height = naver_driver.execute_script("return document.body.scrollHeight")

                            # 늘어난 스크롤 위치와 이동 전 위치 같으면(더 이상 스크롤이 늘어나지 않으면) 종료
                            if scroll_location == scroll_height:
                                break

                            # 같지 않으면 스크롤 위치 값을 수정하여 같아질 때까지 반복
                            else:
                                # 스크롤 위치값을 수정
                                scroll_location = naver_driver.execute_script("return document.body.scrollHeight")

                            naver_driver.implicitly_wait(5)
                            # print('스크롤 내림')

                    except:
                        print('스크롤 안됨')

                    if not naver_driver.find_element(By.XPATH,
                                                     '//*[@id="app-root"]/div/div/div/div[5]/div/div/div/div/a[2]'):
                        break

            except:
                print('더보기 안됨')

            try:
                naver_driver.find_element(By.CLASS_NAME, 'sBWyy')
                naver_driver.implicitly_wait(5)
                print('sBWyy 있음')

                naver_html = naver_driver.page_source
                naver_soup = BeautifulSoup(naver_html, 'lxml')
                naver_driver.implicitly_wait(5)
                print('페이지 소스 가져옴')

                for nic in naver_soup.find_all('div', attrs={'class': 'sBWyy'}):
                    print(nic.text)
                    nic_list.append(nic.text)

                try:
                    naver_driver.implicitly_wait(3)
                    for review in naver_soup.find_all('span', attrs={'class': 'zPfVt'}):
                        print(review.text)
                        re_list.append(review.text)
                except:
                    print('글 리뷰없음')
                    re_list.append('')

                try:
                    naver_driver.implicitly_wait(3)
                    for re_date in naver_soup.find_all('time', attrs={'aria-hidden': 'true'}):
                        print(re_date.text)
                        date_list.append(re_date.text)
                except:
                    print('리뷰 날짜 없음')
                    date_list.append('')

                try:

                    for num in range(len(naver_soup.find_all('a', attrs={'class': 'P1zUJ ZGKcF'}))):
                        #                    for add in naver_driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[3]/div[1]/ul/li[1]/div[3]/a'):
                        naver_driver.find_element(By.XPATH,
                                                  '//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[3]/div[1]/ul/li[' + num + ']/div[3]/a').send_keys(
                            Keys.ENTER)
                        naver_driver.implicitly_wait(3)
                        # add.click()
                        # add.send_
                        print('태그 리뷰 더보기 클릭')

                        for re_tag in naver_soup.find_all('div', attrs={'class': 'gyAGI'}):
                            print(re_tag.text)
                            tag_list.append(re_tag.text)

                except:
                    print('태그 리뷰 더보기 없음')

                    try:
                        for re_tag in naver_soup.find_all('div', attrs={'class': 'gyAGI'}):
                            print(re_tag.text)
                            tag_list.append(re_tag.text)

                    except:
                        print('태그 리뷰 없음')
                        tag_list.append('')



            #                 try:
            #                     naver_soup.find_all('span', attrs = {'class':'P1zUJ.HNG_1'})

            #                     for re_star in naver_soup.find_all('span', attrs = {'class':'P1zUJ.HNG_1'}):
            #                         print(re_star.text)
            #                         re_star_list.append(re_star.text)
            #                 except:
            #                     print('리뷰 별점 없음')
            #                     re_star_list.append('')

            except:
                print('닉네임 없음')
                nic_list.append('')

        except:
            print('리뷰 클릭 안됨')
            nic_list.append('')
            re_list.append('')
            date_list.append('')
            tag_list.append('')

        try:
            is_store_exist = naver_driver.find_element(By.CLASS_NAME, 'FYvSc')

            is_store_exist.text == '조건에 맞는 업체가 없습니다.'
            a = 'x'
            print('x')
            a_list.append(a)
        except:
            pass

        print('\n' * 3)


    except Exception as e1:
        #         pass

        a = 'o'
        print('o')
        a_list.append(a)

#         if "li:nth-child(1)" in str(e1):
#             try:
#                 naver_df.iloc[i,-2] = naver_driver.find_element(By.CLASS_NAME,"XUrfU")
# #                 time.sleep(1)
#             except Exception as e2:
#                 print(e2)
#                 naver_df.iloc[i,-2] = naver_driver.find_element(By.CLASS_NAME,"XUrfU")
#                 time.sleep(1)
#         else:
#             pass


naver_driver.quit()

