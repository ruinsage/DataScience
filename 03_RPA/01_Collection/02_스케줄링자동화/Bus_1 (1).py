# 목적: 파이썬 코드를 활용하여 OpenAPI 호출 자동화
# Step1: OpenAPI를 제공하는 사이트에서 제공하는 샘플 프로그램을 확보한다.
import json
from datetime import datetime
import pandas as pd

# import requests
#
# url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll'
# params ={'serviceKey' : '서비스키', 'busRouteId' : '' }





import requests
# 파이썬에서 돌릴때는 decoding 키값을 입력해야하나?
access_key = 'aZH/fesow7HZNHDNyVGsNGBNDeyd/9TBlzpG3q5/4+uAnjaYX+NETEvp//J6giK/nziOH///JopizVuBZfXSJA=='
def get_request_url():
    url = 'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll'
    params = {'serviceKey': access_key , 'busRouteId' : 100100118,'resultType':'json'}
    response = requests.get(url, params=params)
    # response.content # => response.content는 한글이 인코딩된 형식이므로
    #                       response.text 를 응답받기로함
    return response.text

# def json_to_df_info(parsed_json) :
#     all_data = []
#     column_list = ["stId","stNm","arsId","rtNm","firstTm","lastTm","term","routeType","nextBus",
#                    "dir","vehId1","traTime1","isArrive1","exps1","vehId2","traTime2","isArrive2",
#                    "exps2","arrmsg1","arrmsg2"]
#
#     for record in raw_json['msgBody']['itemList']:
#         all_data.append(
#             {"stId": record.get("stId"),
#              "stNm": record.get("stNm"),
#
#              "arsId": record.get("arsId"),
#              "rtNm": record.get("rtNm"),
#              "firstTm": record.get("firstTm"),
#              "lastTm": record.get("lastTm"),
#              "term": record.get("term"),
#              "routeType": record.get("routeType"),
#              "nextBus": record.get("nextBus"),
#              "dir": record.get("dir"),
#
#              "vehId1": record.get("vehId1"),
#              "traTime1": record.get("traTime1"),
#              "isArrive1": record.get("isArrive1"),
#              "exps1": record.get("exps1"),
#
#              "vehId2": record.get("vehId2"),
#              "traTime2": record.get("traTime2"),
#              "isArrive2": record.get("isArrive2"),
#              "exps2": record.get("exps2"),
#
#              "arrmsg1": record.get("arrmsg1"),
#              "arrmsg2": record.get("arrmsg2"),
#              }
#         )
#
#     return column_list, all_data

def json_to_df_info(parsed_json) :
    all_data = []
    column_list = ["stId","stNm","arsId","rtNm","firstTm","lastTm","term","routeType","nextBus",
                    "dir","vehId1","traTime1","isArrive1","exps1","vehId2","traTime2","isArrive2",
                    "exps2","arrmsg1","arrmsg2"]

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

             "arsId": "정류소번호",
             "rtNm": "노선명",
             "firstTm": "첫차시간",
             "lastTm": "막차시간",
             "term": "배차간격",
             "routeType": "간선버스",
             "nextBus": "막차여부",
             "dir": "방향",

             "vehId1": "첫번째도착예정버스ID",
             "traTime1": "첫번째도착예정버스의여행시간_분",
             "isArrive1": "첫번째버스의정류소도착출발여부",
             "exps1": "첫번째버스의도착예정시간",

             "vehId2": "두번째도착예정버스ID",
             "traTime2": "두번째도착예정버스의여행시간_분",
             "isArrive2": "2버스정류소도착출발여부",
             "exps2": "2버스도착시간",

             "arrmsg1": "첫번째도착정보메시지",
             "arrmsg2": "두번째도착정보메시지"
    }, inplace=True)

    redefined_columns = ["정류소ID","정류소명","정류소번호","노선명","첫차시간","막차시간","배차간격",
                         "간선버스","막차여부","방향",
                         "첫번째도착예정버스ID","첫번째도착예정버스의여행시간_분","첫번째버스의정류소도착출발여부","첫번째버스의도착예정시간",
                         "두번째도착예정버스ID","두번째도착예정버스의여행시간_분","2버스정류소도착출발여부","2버스도착시간",
                         "첫번째도착정보메시지","두번째도착정보메시지"]
    df = df[redefined_columns]
    return df

raw_str_json = get_request_url()


if raw_str_json :
    # json.loads() 문자열 json을 실제 json(dict) 타입으로 변환
    raw_json = json.loads(raw_str_json)

column_list, all_data = json_to_df_info(raw_json)
now = datetime.now()

#file_name = f'서울특별시_753번_버스도착정보조회_{now.strftime("%Y/%m/%d/%H:%M:%S")}.json'
file_name = '서울특별시_753번_버스도착정보조회.csv'

# print(parsed_json)
# with open(file_name, 'w', encoding='utf8') as outfile:
#     retJson = json.dumps(parsed_json, indent=4, sort_keys=False, ensure_ascii=False)
#
#     outfile.write(retJson)
#
# print(f'{file_name} SAVED\n')

df = pd.DataFrame(all_data, columns=column_list)

df_preprosessed = preprocessed_df(df)

df_preprosessed.to_csv(file_name, index=False, encoding='cp949')