import json
import time
import pandas
import requests

url = 'http://api.jejuits.go.kr/api/infoParkingStateList'
key = 860553
date = 20230104

def get_request_url(url):
    params = {'code': key}
    response = requests.get(url, params=params)
    return response.text

#print(get_request_url(url))

def json_to_df_park(raw_json):
    all_data = []
    column_list = ['id', 'gnrl', 'lgvh', 'hvvh', 'emvh', 'hndc', 'wmon', 'etc']

    for record in raw_json['info']:
        row_data = []
        for column_data in column_list:
            row_data.append(record.get(column_data))
        all_data.append(row_data)

    column_list = ['주차장ID', '일반', '경차', '대형', '긴급차량', '장애인', '여성', '기타']
    return column_list, all_data


# {"id":"16489518","gnrl":72,"lgvh":4,"hvvh":0,"emvh":0,"hndc":3,"wmon":0,"etc":0}
# id	주차장 ID
# gnrl	일반 잔여 주차구역 개수
# lgvh	경차 잔여 주차구역 개수
# hvvh	대형 잔여 주차구역 개수
# emvh	긴급차량 잔여 주차구역 개수
# hndc	장애인 잔여 주차구역 개수
# wmon	여성전용 잔여 주차구역 개수
# etc	기타 잔여 주차구역 개수
def park_info_collector():
    raw_str_json = get_request_url(url)

    if raw_str_json:
        raw_json = json.loads(raw_str_json)

    column_list, all_data = json_to_df_park(raw_json)

    df = pandas.DataFrame(all_data, columns=column_list)
    print(df)
    #preprocessed_df_to_oracle(df)

def park_info_scheduler():
    print('데이터 수집기 스케줄러 동작.\n')
    while True:
        park_info_collector()
        print("1시간 주기 수집중")
        time.sleep(3600)


park_info_scheduler()