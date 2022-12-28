import threading
import time
import requests
import json
from datetime import datetime, timedelta

import pandas as pd
import cx_Oracle

access_key = 'aZH/fesow7HZNHDNyVGsNGBNDeyd/9TBlzpG3q5/4+uAnjaYX+NETEvp//J6giK/nziOH///JopizVuBZfXSJA=='

print('< 버스운행정보 데이터 수집기 ver1.0>')

def get_request_url(url):
    params = {'serviceKey': access_key , 'busRouteId' : 100100118,'resultType': 'json'}
    response = requests.get(url, params=params)
    return response.text

def json_to_df_info(raw_json):
    all_data = []
    column_list = ["stId","stNm",
                   # "arsId","rtNm","firstTm","lastTm","term","routeType","nextBus",
                   #  "dir","vehId1","traTime1","isArrive1","exps1","vehId2","traTime2","isArrive2",
                   #  "exps2",
                   "arrmsg1","arrmsg2"]

    for record in raw_json['msgBody']['itemList'] :
        row_data = []
        for column_data in column_list:
            row_data.append(record.get(column_data))
        all_data.append(row_data)

    return column_list, all_data

def preprocess_df(df):

    df.rename(columns={
         "stId": "정류소ID",
             "stNm": "정류소명",

             # "arsId": "정류소번호",
             # "rtNm": "노선명",
             # "firstTm": "첫차시간",
             # "lastTm": "막차시간",
             # "term": "배차간격",
             # "routeType": "간선버스",
             # "nextBus": "막차여부",
             # "dir": "방향",
             #
             # "vehId1": "첫번째도착예정버스ID",
             # "traTime1": "첫번째도착예정버스의여행시간_분",
             # "isArrive1": "첫번째버스의정류소도착출발여부",
             # "exps1": "첫번째버스의도착예정시간",
             #
             # "vehId2": "두번째도착예정버스ID",
             # "traTime2": "두번째도착예정버스의여행시간_분",
             # "isArrive2": "두번째버스정류소도착출발여부",
             # "exps2": "두번째버스도착시간",

             "arrmsg1": "첫번째도착정보메시지",
             "arrmsg2": "두번째도착정보메시지"
    }, inplace=True)

    redefined_columns = ["정류소ID","정류소명",
                         # "정류소번호","노선명","첫차시간","막차시간","배차간격", "간선버스","막차여부","방향",
                         # "첫번째도착예정버스ID","첫번째도착예정버스의여행시간_분","첫번째버스의정류소도착출발여부","첫번째버스의도착예정시간",
                         # "두번째도착예정버스ID","두번째도착예정버스의여행시간_분","두번째버스정류소도착출발여부","두번째버스도착시간",
                         "첫번째도착정보메시지","두번째도착정보메시지"]
    p_df = df[redefined_columns]
    return p_df

def preprocessed_df_to_oracle(df):
    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    df_range = df.shape[0]

    for record in range(df_range):
        sql_insert = '''insert into bus(정류소ID,정류소명,첫번째도착정보메시지,두번째도착정보메시지) 
            values(:정류소ID,:정류소명,:첫번째도착정보메시지,:두번째도착정보메시지)'''
        # 정류소번호, 노선명, 첫차시간, 막차시간,
        # 배차간격, 간선버스, 막차여부, 방향,
        # 첫번째도착예정버스ID, 첫번째도착예정버스의여행시간_분, 첫번째버스의정류소도착출발여부, 첫번째버스의도착예정시간,
        # 두번째도착예정버스ID, 두번째도착예정버스의여행시간_분, 두번째버스정류소도착출발여부, 두번째버스도착시간,

        # :정류소번호,:노선명,:첫차시간,:막차시간,:배차간격,:간선버스,:막차여부,:방향,
        # :첫번째도착예정버스ID,:첫번째도착예정버스의여행시간_분,:첫번째버스의정류소도착출발여부,:첫번째버스의도착예정시간",
        # :두번째도착예정버스ID,:두번째도착예정버스의여행시간_분,:두번째버스정류소도착출발여부,:두번째버스도착시간,

        정류소ID = df.iloc[record]['정류소ID']
        정류소명 = df.iloc[record]['정류소명']
        # 정류소번호 = int(df.iloc[0]['정류소번호'])
        # 노선명 = df.iloc[0]['노선명']
        # 첫차시간 = df.iloc[0]['첫차시간']
        # 막차시간 = df.iloc[0]['막차시간']
        # 배차간격 = df.iloc[0]['배차간격']
        # 간선버스 = df.iloc[0]['간선버스']
        # 막차여부 = df.iloc[0]['막차여부']
        # 방향 = df.iloc[0]['방향']
        # 첫번째도착예정버스ID = df.iloc[0]['첫번째도착예정버스ID']
        # 첫번째도착예정버스의여행시간_분 = df.iloc[0]['첫번째도착예정버스의여행시간_분']
        # 첫번째버스의정류소도착출발여부 = df.iloc[0]['첫번째버스의정류소도착출발여부']
        # 첫번째버스의도착예정시간 = df.iloc[0]['첫번째버스의도착예정시간']
        # 두번째도착예정버스ID = df.iloc[0]['두번째도착예정버스ID']
        # 두번째도착예정버스의여행시간_분 = df.iloc[0]['두번째도착예정버스의여행시간_분']
        #
        # 두번째버스정류소도착출발여부 = df.iloc[0]['두번째버스정류소도착출발여부']
        # 두번째버스도착시간 = df.iloc[0]['두번째버스도착시간']
        첫번째도착정보메시지 = df.iloc[record]['첫번째도착정보메시지']
        두번째도착정보메시지 = df.iloc[record]['두번째도착정보메시지']
        제공시각 = df.iloc[record]['제공시각']
        cur.execute(sql_insert,
                (   정류소ID,정류소명,
                    # 정류소번호,노선명,첫차시간,막차시간,배차간격,간선버스,막차여부,방향,첫번째도착예정버스ID,첫번째도착예정버스의여행시간_분,
                    # 첫번째버스의정류소도착출발여부,첫번째버스의도착예정시간,두번째도착예정버스ID,두번째도착예정버스의여행시간_분,두번째버스정류소도착출발여부,
                    # 두번째버스도착시간,
                    첫번째도착정보메시지,두번째도착정보메시지,제공시각)
                )

    con.commit()
    cur.close()
    con.close()


def bus_info_collector():
    url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll'

    # busRouteId = 100100118
    # resultType = json

    raw_str_json = get_request_url(url)

    if raw_str_json:
        raw_json = json.loads(raw_str_json)

    column_list, all_data = json_to_df_info(raw_json)

    df = pd.DataFrame(all_data, columns=column_list)

    df_preprocessed = preprocess_df(df)

    preprocessed_df_to_oracle(df_preprocessed)

bus_info_collector()
# def bus_info_scheduler():
#     print('기상정보 수집기 스케줄러 동작.\n')
#     while True:
#         bus_info_collector()
#         print("수집완료.")
#         time.sleep(60) # 1시간 주기로 데이터 수집
#
# def print_main_menu():
#     print('\n1. 버스 실시간 데이터 구축')
#     print('2. 스케줄러 종료')
#     print('* 엔터: 메뉴 업데이트\n')
#
# while True:
#     print_main_menu()
#     print('아래행에 메뉴입력: ')
#     selection = input()
#     if selection == '':  continue
#     else:                menu_num = int(selection)
#
#     if(menu_num == 1):
#         t = threading.Thread(target=bus_info_scheduler, daemon=True)
#         t.start()
#     elif(menu_num == 2):
#         break
#     elif (menu_num == 0):
#         continue
