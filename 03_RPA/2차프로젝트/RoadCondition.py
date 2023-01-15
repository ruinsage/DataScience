import requests
import json
import time
import cx_Oracle
import pandas as pd

code = '860553'
def get_request_url():
    url = 'http://api.jejuits.go.kr/api/infoRwisList'
    params = {'code': code}
    response = requests.get(url, params=params)
    return response.text
def to_oracle() :
    raw_json = json.loads(get_request_url())

    if len(raw_json['info']) > 0 :
        current_time = time.strftime('%Y-%m-%d %H:%M:%S')

        con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
        cur = con.cursor()
        query = 'insert into ROAD_CONDITION values (ROAD_CONDITION_SEQ.NEXTVAL, :lat, :lon, :heading, :link_id, :visibility, :snow, :road_temp, :water_film, :friction, :code, :current_time)'

        for info in raw_json['info'] :
            lat = info.get("latitude")
            lon = info.get("longitude")
            heading = info.get("heading")
            link_id = info.get("link_id")
            visibility = info.get("visibility")
            snow = info.get("snow")
            road_temp = info.get("road_temp")
            water_film = info.get("water_film")
            friction = info.get("friction")
            code = info.get("code")

            cur.execute(query, (lat, lon, heading, link_id, visibility, snow, road_temp, water_film, friction, code, current_time))

        con.commit()
        cur.close()
        con.close()

def make_df() :
    input_file = 'RoadCondition.xlsx'
    df = pd.read_excel(input_file, sheet_name='herricane')
    print(df)
    return df

def hericane_data_to_oracle(df) :
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    query = 'insert into ROAD_CONDITION values (ROAD_CONDITION_SEQ.NEXTVAL, :lat, :lon, :heading, :link_id, :visibility, :snow, :road_temp, :water_film, :friction, :code, :current_time)'


    for i in range(len(df)):
        lat = int(df.iloc[i]["latitude"])
        lon = int(df.iloc[i]["longitude"])
        heading = int(df.iloc[i]["heading"])
        link_id = int(df.iloc[i]["link_id"])
        visibility = int(df.iloc[i]["visibility"])
        snow = int(df.iloc[i]["snow"])
        road_temp = int(df.iloc[i]["road_temp"])
        water_film = int(df.iloc[i]["water_film"])
        friction = int(df.iloc[i]["friction"])
        code = int(df.iloc[i]["code"])

        cur.execute(query, (lat, lon, heading, link_id, visibility, snow, road_temp, water_film, friction, code, current_time))

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