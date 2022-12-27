# 목적: 파싱된 JSON 파일 저장

import requests
import datetime
import time
import json

# Encoding key
# access_key = 'pnWEl7Muj6PpSyrC35SaqRjYnKAAL0xedWtDdUQDmfsWvqDxK1ORAkSg2%2FaxQsJNCKZjQlf98A3TRAuuIzJ0GQ%3D%3D'
# Decoding key
access_key = 'pnWEl7Muj6PpSyrC35SaqRjYnKAAL0xedWtDdUQDmfsWvqDxK1ORAkSg2/axQsJNCKZjQlf98A3TRAuuIzJ0GQ=='

def get_request_url():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {'serviceKey': access_key,'numOfRows': 10,'pageNo': 1,
        'dataType' : 'JSON', 'base_date' : base_date , 'base_time' : day_time, 'nx' : x_coodinate, 'ny' : y_coodinate
        }
    response = requests.get(url, params=params)
    # response.content # => response.content는 한글이 인코딩된 형식이므로
    #                       response.text를 응답받기로 함
    return response.text

def get_parsed_json(raw_json):
    all_data = []
    for record in raw_json['response']['body']['items']['item']:
        all_data.append(
        {"baseDate": record.get("baseDate"),
         # "baseDate": record["baseDate"],  # 이 코드도 dict타입의 value를 가져오는 코드
         "baseTime": record.get("baseTime"),
         "category": record.get("category"),
         "nx": record.get("nx"),
         "ny": record.get("ny"),
         "obsrValue": record.get("obsrValue")}
        )
    return all_data


#yyyymmdd = 20221227
day_time = 1102
base_date = time.strftime('%Y%m%d')
#day_time = time.strftime('%H%M')
# 00분~40분 구간은 최신 정보가 없음
# 41분~59분 구간은 최신 정보가 있음
# new_day_time = str(int(day_time) - 80)
# print(new_day_time)
# 구로구 구로동 좌표
x_coodinate = 58
y_coodinate = 125
raw_str_json = get_request_url()

if raw_str_json:
    raw_json = json.loads(raw_str_json) # json.loads()문자열 json을 실제 json(dict)으로 변환해준다

parsed_json = get_parsed_json(raw_json)
print(parsed_json)

file_name = f'초단기날씨현황_조회_{base_date}{day_time}.json'

with open(file_name, 'w', encoding='utf8') as outfile:
    retJson = json.dumps(parsed_json, indent=4, sort_keys=True, ensure_ascii=False)

    outfile.write(retJson)

print(f'{file_name} SAVED\n')