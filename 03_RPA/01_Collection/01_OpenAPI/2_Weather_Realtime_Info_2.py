# 목적: 파라메터 변수화

import requests
import datetime
import time

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

#yyyymmdd = 20221227
#day_time = 1049
base_date = time.strftime('%Y%m%d')
day_time = time.strftime('%H%M')
# 00분~40분 구간은 최신 정보가 없음
# 41분~59분 구간은 최신 정보가 있음
# new_day_time = str(int(day_time) - 80)
# print(new_day_time)
# 구로구 구로동 좌표
x_coodinate = 58
y_coodinate = 125
raw_json = get_request_url()
print(raw_json)
