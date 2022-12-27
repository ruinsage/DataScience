# 목적: 파이썬 코드를 활용하여 OpenAPI 호출 자동화
# Step1: OpenAPI를 제공하는 사이트에서 제공하는 샘플 프로그램을 확보한다.

# 샘플 프로그램
# import requests

# url = 'http://apis.data.go.kr/B551177/StatusOfArrivals/getArrivalsCongestion'
# params ={'serviceKey' : '서비스키', 'numOfRows' : '10', 'pageNo' : '1', 'terno' : 'T1', 'airport' : 'HAN', 'type' : 'xml' }
#
# response = requests.get(url, params=params)
# print(response.content)

import requests
# Encoding key
# access_key = 'pnWEl7Muj6PpSyrC35SaqRjYnKAAL0xedWtDdUQDmfsWvqDxK1ORAkSg2%2FaxQsJNCKZjQlf98A3TRAuuIzJ0GQ%3D%3D'
# Decoding key
access_key = 'pnWEl7Muj6PpSyrC35SaqRjYnKAAL0xedWtDdUQDmfsWvqDxK1ORAkSg2/axQsJNCKZjQlf98A3TRAuuIzJ0GQ=='
def get_request_url():
    url = 'http://library.me.go.kr/pyxis-api/2/collections/2/search?all=k|a|library'
    params = {'serviceKey': access_key,'numOfRows': 10,'pageNo': 1,
        'dataType' : 'JSON', 'base_date' : 20221227 , 'base_time' : 1049, 'nx' : 58, 'ny' : 125
        }
    response = requests.get(url)
    # response.content # => response.content는 한글이 인코딩된 형식이므로
    #                       response.text를 응답받기로 함
    return response.text

raw_json = get_request_url()
print(raw_json)
