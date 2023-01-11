import json
import threading
import time
import cx_Oracle
import pandas
import requests

service_key = 'hRfuERzasg3WVKibaLkKQ=='
url = 'http://www.khoa.go.kr/api/oceangrid/obsWaveHight/search.do'
date = 20230103
obs_jeju = {'KG_0021': '제주남부', 'KG_0028': '제주해협'}
def get_request_url(url, ObsCode):
    params = {'ServiceKey': service_key, 'ObsCode': ObsCode, 'Date': date, 'ResultType': 'json'}
    response = requests.get(url, params=params)
    return response.text

def json_to_df_wave(ObsCode, raw_json):
    all_data = []
    column_list = ['record_time', 'wave_height']

    for record in raw_json['result']['data']:
        row_data = []
        row_data.append(ObsCode)
        row_data.append(obs_jeju[ObsCode])

        for column_data in column_list:
            row_data.append(record.get(column_data))
        all_data.append(row_data)

    column_list = ['관측소코드', '관측소명', '관측시간', '파도높이']
    print(all_data)
    return column_list, all_data

def preprocessed_df_to_oracle(df):
    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    sql_insert = 'insert into wave2 values(:관측소코드,:관측소명,:관측시간,:파도높이)'
    관측소코드 = df.iloc[len(df)-1]['관측소코드']
    관측소명 = df.iloc[len(df)-1]['관측소명']
    관측시간 = df.iloc[len(df)-1]['관측시간']
    파도높이 = df.iloc[len(df)-1]['파도높이']

    cur.execute(sql_insert, (관측소코드, 관측소명, 관측시간, 파도높이))
    con.commit()
    cur.close()
    con.close()

def wave_info_collector():
    for ObsCode in obs_jeju:
        raw_str_json = get_request_url(url, ObsCode)

        if raw_str_json:
            raw_json = json.loads(raw_str_json)

        column_list, all_data = json_to_df_wave(ObsCode, raw_json)

        df = pandas.DataFrame(all_data, columns=column_list)
        print(df)
        preprocessed_df_to_oracle(df)

def wave_info_scheduler():
    print('데이터 수집기 스케줄러 동작.\n')
    while True:
        wave_info_collector()
        print("수집완료.")
        time.sleep(1860)    # 31분

def print_main_menu():
    print('\n1. 실시간 파고 데이터 구축')
    print('2. 스케줄러 종료')
    print('* 엔터: 메뉴 업데이트\n')

while True:
    print_main_menu()
    print('아래행에 메뉴입력: ')
    selection = input()
    if selection == '': continue
    else:                menu_num = int(selection)

    if(menu_num == 1):
        t = threading.Thread(target=wave_info_scheduler, daemon=True)
        t.start()
    elif(menu_num == 2):
        break
    elif (menu_num == 0):
        continue