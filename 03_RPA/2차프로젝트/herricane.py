import requests
import json
import time
import cx_Oracle
import pandas as pd

def make_RoadWork_df() :
    input_file = 'herricane.xlsx'
    RoadWork_df = pd.read_excel(input_file, sheet_name='RoadWork')
    print(RoadWork_df)
    return RoadWork_df

def hericane_RoadWork_to_oracle(RoadWork) :
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    query = 'merge into ROAD_WORK ' \
            'using DUAL on (id = :ocrr_id) ' \
            'when matched then ' \
            'update set last_updated_at = :current_time ' \
            'when not matched then ' \
            'insert (id, lat, lon, heading, link_id, whole_lane, block_lane, text, created_at, last_updated_at) ' \
            'values (:ocrr_id, :lat, :lon, :heading, :link_id, :whole_lane, :block_lane, :text, :current_time, :current_time)'

    for i in range(len(RoadWork)):
        ocrr_id = int(RoadWork.iloc[i]['ocrr_id'])
        lat = int(RoadWork.iloc[i]['latitude'])  # int 값에 대해서는 int 형으로 변환해줘야 한다.
        lon = int(RoadWork.iloc[i]['longitude'])
        heading = int(RoadWork.iloc[i]['heading'])
        link_id = int(RoadWork.iloc[i]['link_id'])
        whole_lane = int(RoadWork.iloc[i]['whole_lane'])
        block_lane = int(RoadWork.iloc[i]['block_lane'])
        text = RoadWork.iloc[i]['text']

        cur.execute(query, (ocrr_id, current_time, ocrr_id, lat, lon, heading, link_id, whole_lane, block_lane, text, current_time, current_time))

    con.commit()
    cur.close()
    con.close()

def make_ROADEVENT_df() :
    input_file = 'herricane.xlsx'
    ROADEVENT_df = pd.read_excel(input_file, sheet_name='ROADEVENT')
    print(ROADEVENT_df)
    return ROADEVENT_df

def hericane_ROADEVENT_to_oracle(ROADEVENT_df) :
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

    for i in range(len(ROADEVENT_df)):
        ocrr_id = ROADEVENT_df.iloc[i]["ocrr_id"]
        lat = int(ROADEVENT_df.iloc[i]["latitude"])
        lon = int(ROADEVENT_df.iloc[i]["longitude"])
        heading = int(ROADEVENT_df.iloc[i]["heading"])
        link_id = int(ROADEVENT_df.iloc[i]["link_id"])
        code = int(ROADEVENT_df.iloc[i]["code"])

        cur.execute(query, (ocrr_id, current_time, ocrr_id, lat, lon, heading, link_id, code, current_time, current_time))

    con.commit()
    cur.close()
    con.close()

def make_RoadCondition_df() :
    input_file = 'herricane.xlsx'
    RoadCondition_df = pd.read_excel(input_file, sheet_name='RoadCondition')
    print(RoadCondition_df)
    return RoadCondition_df

def hericane_RoadCondition_to_oracle(RoadCondition_df) :
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    query = 'insert into ROAD_CONDITION values (ROAD_CONDITION_SEQ.NEXTVAL, :lat, :lon, :heading, :link_id, :visibility, :snow, :road_temp, :water_film, :friction, :code, :current_time)'


    for i in range(len(RoadCondition_df)):
        lat = int(RoadCondition_df.iloc[i]["latitude"])
        lon = int(RoadCondition_df.iloc[i]["longitude"])
        heading = int(RoadCondition_df.iloc[i]["heading"])
        link_id = int(RoadCondition_df.iloc[i]["link_id"])
        visibility = int(RoadCondition_df.iloc[i]["visibility"])
        snow = int(RoadCondition_df.iloc[i]["snow"])
        road_temp = int(RoadCondition_df.iloc[i]["road_temp"])
        water_film = int(RoadCondition_df.iloc[i]["water_film"])
        friction = int(RoadCondition_df.iloc[i]["friction"])
        code = int(RoadCondition_df.iloc[i]["code"])

        cur.execute(query, (lat, lon, heading, link_id, visibility, snow, road_temp, water_film, friction, code, current_time))

    con.commit()
    cur.close()
    con.close()

def make_RoadClose_df() :
    input_file = 'herricane.xlsx'
    RoadClose_df = pd.read_excel(input_file, sheet_name='RoadClose')
    print(RoadClose_df)
    return RoadClose_df

def hericane_RoadClose_to_oracle(RoadClose_df) :
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    query = 'merge into ROAD_CLOSE ' \
            'using DUAL on (id = :ocrr_id) ' \
            'when matched then ' \
            'update set last_updated_at = :current_time ' \
            'when not matched then ' \
            'insert (id, lat, lon, heading, link_id, whole_lane, block_lane, text, created_at, last_updated_at) ' \
            'values (:ocrr_id, :lat, :lon, :heading, :link_id, :whole_lane, :block_lane, :text, :current_time, :current_time)'

    for i in range(len(RoadClose_df)):
        ocrr_id = int(RoadClose_df.iloc[i]['ocrr_id'])
        lat = int(RoadClose_df.iloc[i]['latitude'])  # int 값에 대해서는 int 형으로 변환해줘야 한다.
        lon = int(RoadClose_df.iloc[i]['longitude'])
        heading = int(RoadClose_df.iloc[i]['heading'])
        link_id = int(RoadClose_df.iloc[i]['link_id'])
        whole_lane = int(RoadClose_df.iloc[i]['whole_lane'])
        block_lane = int(RoadClose_df.iloc[i]['block_lane'])
        text = RoadClose_df.iloc[i]['text']

        cur.execute(query, (ocrr_id, current_time, ocrr_id, lat, lon, heading, link_id, whole_lane, block_lane, text, current_time, current_time))

    con.commit()
    cur.close()
    con.close()

def make_wave_df() :
    input_file = 'herricane.xlsx'
    wave_df = pd.read_excel(input_file, sheet_name='wave')
    print(wave_df)
    return wave_df

def wave_df_to_oracle(wave_df):
    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    lat_list= ['32.09','33.7']
    lon_list = ['126.965','126.59']
    sql_insert = 'insert into wave2 values(:관측소코드,:관측소명,:관측시간,:파도높이)'

    for i in range(len(wave_df)):
        관측소코드 = wave_df.iloc[i]['관측소코드']
        관측소명 = wave_df.iloc[i]['관측소명']
        관측시간 = time.strftime('%Y-%m-%d %H:%M:%S',(wave_df.iloc[i]['관측시간']))
        파도높이 = int(wave_df.iloc[i]['파도높이'])
        lat = lat_list[i]
        lon = lon_list[i]

    cur.execute(sql_insert, (관측소코드, 관측소명, 관측시간, 파도높이,lat, lon))
    con.commit()
    cur.close()
    con.close()


def print_main_menu():
    print('\n1. 태풍 시뮬레이션 데이터 구축')
    print('2. 스케줄러 종료')
    print('* 엔터: 메뉴 업데이트\n')


while True:
    print_main_menu()
    print('아래행에 메뉴입력: ')
    selection = input()
    if selection == '':  continue
    else:                menu_num = int(selection)

    if(menu_num == 1):
        hericane_ROADEVENT_to_oracle(make_ROADEVENT_df())
        hericane_RoadWork_to_oracle(make_RoadWork_df())
        hericane_RoadCondition_to_oracle(make_RoadCondition_df())
        hericane_RoadClose_to_oracle(make_RoadClose_df())
        #wave_df_to_oracle(make_wave_df())
    elif(menu_num == 2):
        break
    elif (menu_num == 0):
        continue







