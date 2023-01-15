import requests
import json
import time
import cx_Oracle
import pandas as pd

code = '860553'
def get_request_url():
    url = 'http://api.jejuits.go.kr/api/infoRoadEventList'
    params = {'code': code}
    response = requests.get(url, params=params)
    return response.text
def to_oracle() :
    raw_json = json.loads(get_request_url())

    print(len(raw_json['info']))

    if len(raw_json['info']) > 0 :
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')

        con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
        cur = con.cursor()
        query = 'merge into ROAD_EVENT ' \
                'using DUAL on (id = :ocrr_id) ' \
                'when matched then ' \
                'update set last_updated_at = :current_time ' \
                'when not matched then ' \
                'insert (id, lat, lon, heading, link_id, code, created_at, last_updated_at) ' \
                'values (:ocrr_id, :lat, :lon, :heading, :link_id, :code, :current_time, :current_time)'

        for info in raw_json['info'] :
            ocrr_id = info.get("ocrr_id")
            lat = info.get("latitude")
            lon = info.get("longitude")
            heading = info.get("heading")
            link_id = info.get("link_id")
            code = info.get("code")

            print(ocrr_id)

            cur.execute(query, (ocrr_id, current_time, ocrr_id, lat, lon, heading, link_id, code, current_time, current_time))

        con.commit()
        cur.close()
        con.close()

def make_df() :
    input_file = 'ROADEVENT.xlsx'
    df = pd.read_excel(input_file, sheet_name='herricane')
    print(df)
    return df

def hericane_data_to_oracle(df) :
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    query = 'merge into ROAD_EVENT ' \
            'using DUAL on (id = :ocrr_id) ' \
            'when matched then ' \
            'update set last_updated_at = :current_time ' \
            'when not matched then ' \
            'insert (id, lat, lon, heading, link_id, code, created_at, last_updated_at) ' \
            'values (:ocrr_id, :lat, :lon, :heading, :link_id, :code, :current_time, :current_time)'

    for i in range(len(df)):
        ocrr_id = df.iloc[i]["ocrr_id"]
        lat = int(df.iloc[i]["latitude"])
        lon = int(df.iloc[i]["longitude"])
        heading = int(df.iloc[i]["heading"])
        link_id = int(df.iloc[i]["link_id"])
        code = int(df.iloc[i]["code"])

        cur.execute(query, (ocrr_id, current_time, ocrr_id, lat, lon, heading, link_id, code, current_time, current_time))

    con.commit()
    cur.close()
    con.close()



def scheduler():
    print('데이터 수집기 스케줄러 동작.\n')
    while True:
        to_oracle()
        print("수집완료.")
        time.sleep(300)

def print_main_menu():
    print('\n1. 실시간 데이터 구축')
    print('2. 태풍 시뮬레이션 데이터 구축')
    print('3. 스케줄러 종료')
    print('* 엔터: 메뉴 업데이트\n')

while True:
    print_main_menu()
    print('아래행에 메뉴입력: ')
    selection = input()
    if selection == '':  continue
    else:                menu_num = int(selection)

    if(menu_num == 1):
        scheduler()
    elif(menu_num == 2):
        hericane_data_to_oracle(make_df())
    elif (menu_num == 0):
        continue