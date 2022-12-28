import threading
import time
import requests
import json
from datetime import datetime, timedelta

import pandas as pd
import cx_Oracle

access_key = 'aZH/fesow7HZNHDNyVGsNGBNDeyd/9TBlzpG3q5/4+uAnjaYX+NETEvp//J6giK/nziOH///JopizVuBZfXSJA=='

def get_request_url():
    url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll'
    params = {'serviceKey': access_key , 'busRouteId' : 100100118,'resultType':'json'}
    response = requests.get(url, params=params)
    # response.content # => response.content는 한글이 인코딩된 형식이므로
    #                       response.text 를 응답받기로함
    return response.text

def json_to_df_info(parsed_json) :
    raw_str_json = get_request_url()
    if raw_str_json:
        # json.loads() 문자열 json을 실제 json(dict) 타입으로 변환
        raw_json = json.loads(raw_str_json)

    all_data = []
    column_list = ["stId", "stNm", "arrmsg1","arrmsg2","mkTm"]

    for record in raw_json['msgBody']['itemList'] :
        row_data = []
        for column_data in column_list :
            row_data.append(record.get(column_data))
        all_data.append(row_data)
    return column_list, all_data

def preprocessed_df(df) :
    df.rename(columns={
             "stId": "정류소ID",
             "stNm": "정류소명",

             #"arsId": "정류소번호",

             #"exps1": "첫번째버스의도착예정시간",

             #"exps2": "2버스도착시간",
        "arrmsg1": "첫번째도착정보메시지",
        "arrmsg2": "두번째도착정보메시지",
        "mkTm" : "제공시각"
    }, inplace=True)

    redefined_columns = ["정류소ID","정류소명","첫번째도착정보메시지","두번째도착정보메시지","제공시각"]
    df = df[redefined_columns]
    return df

def preprocessed_df_to_oracle(df):
    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    sql_insert = '''
            insert into bus_753(정류소ID,정류소명,첫번째도착정보메시지,두번째도착정보메시지,제공시각) 
            values(:정류소ID, :정류소명, :첫번째도착정보메시지, :두번째도착정보메시지, :제공시각)
            '''
    for i in range(len(df)-1):
        정류소ID = df.iloc[i]['정류소ID']
        정류소명 = df.iloc[i]['정류소명']  # int 값에 대해서는 int 형으로 변환해줘야 한다.
        첫번째도착정보메시지 = df.iloc[i]['첫번째도착정보메시지']
        두번째도착정보메시지 = df.iloc[i]['두번째도착정보메시지']
        제공시각 = df.iloc[i]['제공시각']


        cur.execute(sql_insert,
                (정류소ID,정류소명,첫번째도착정보메시지,두번째도착정보메시지,제공시각 )
                )

    con.commit()
    cur.close()
    con.close()

def Bus_info_collector():

    raw_str_json = get_request_url()

    if raw_str_json:
        raw_json = json.loads(raw_str_json)

    column_list, all_data = json_to_df_info(raw_json)

    df = pd.DataFrame(all_data, columns=column_list)

    df_preprocessed = preprocessed_df(df)

    preprocessed_df_to_oracle(df_preprocessed)


def bus_info_scheduler():
    print('753번 노선 데이터 수집기 스케줄러 동작.\n')
    while True:
        Bus_info_collector()
        print("수집완료.")
        time.sleep(60) # 1분 주기로 데이터 수집

def print_main_menu():
    print('\n1. 753번 노선 실시간 데이터 구축')
    print('2. 스케줄러 종료')
    print('* 엔터: 메뉴 업데이트\n')

while True:
    print_main_menu()
    print('아래행에 메뉴입력: ')
    selection = input()
    if selection == '':  continue
    else:                menu_num = int(selection)

    if(menu_num == 1):
        t = threading.Thread(target=bus_info_scheduler, daemon=True)
        t.start()
    elif(menu_num == 2):
        break
    elif (menu_num == 0):
        continue