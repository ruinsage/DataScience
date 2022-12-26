# 목적: OpenAPI 수집 대용량 데이터에 대한 페이징 테스트
# Step1: OpenAPI를 제공하는 사이트에서 제공하는 샘플 프로그램을 확보한다.

import requests
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring

access_key = 'pnWEl7Muj6PpSyrC35SaqRjYnKAAL0xedWtDdUQDmfsWvqDxK1ORAkSg2/axQsJNCKZjQlf98A3TRAuuIzJ0GQ=='
TOTAL_NUM = 75
MAX_TRANSACTION = 30
target_year = 2020
def get_request_url(page_no):
    url = 'http://apis.data.go.kr/1480802/iciscsc/csclist'
    params = {'serviceKey': access_key,'numOfRows': MAX_TRANSACTION,'pageNo': page_no, 'yyyy' : target_year}
    response = requests.get(url, params=params)
    return response.text

request_total_num = ( TOTAL_NUM // MAX_TRANSACTION) + 1
for page_no in range(1, request_total_num+1):
    raw_xml = get_request_url(page_no)
    parse_xml = fromstring(raw_xml)
    ElementTree(parse_xml).write(f'화학사고정보_응답_page{page_no}.xml', encoding= 'utf-8')
