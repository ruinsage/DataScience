import json
import threading
import time
import cx_Oracle
import pandas
import requests

#https://open.jejudatahub.net/api/proxy/5D5a577taba7tbb71at1b1bt9tatata9/1j1ptb89pcpb7e_2b7r2t9tcto19p_89?
# startDate=20180101
# &endDate=20180131
# &limit=100
# &number=2
# &userType=%EB%82%B4%EA%B5%AD%EC%9D%B8%EA%B4%80%EA%B4%91%EA%B0%9D

url = 'https://open.jejudatahub.net/api/proxy/5D5a577taba7tbb71at1b1bt9tatata9/11j681t1o_ep_91rtj11j1otp11o1e81?'
def get_request_url(url):
    i=2
    params = {'startDate': 20160901, 'endDate': 20181231, 'limit': 100, 'number': i, 'userType': '내국인관광객'}
    response = requests.get(url, params=params)
    return response.text

def json_to_df(raw_json):
    all_data = []
    column_list = ['sido', 'sigungu', 'cityGubun', 'marketType', 'ageGroup', 'gender', 'dtYearMonth', 'userCount', 'useCount', 'useCost']

    for record in raw_json['data']:
        row_data = []
        for column_data in column_list:
            row_data.append(record.get(column_data))
        all_data.append(row_data)

    column_list = ['시도', '시군구', '읍면동', '업종', '연령대', '성별', '날짜', '이용자수', '이용횟수', '이용액']
    return column_list, all_data

def info_collector():
    raw_str_json = get_request_url(url)

    if raw_str_json:
        raw_json = json.loads(raw_str_json)

    column_list, all_data = json_to_df(raw_json)

    df = pandas.DataFrame(all_data, columns=column_list)
    print(df)
    df.to_csv('credit_card2.csv', encoding='cp949', index=False)

info_collector()
