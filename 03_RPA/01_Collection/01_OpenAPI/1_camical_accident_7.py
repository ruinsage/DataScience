# 목적: 전체 수집 데이터를 데이터 프레임으로 전환

import pandas as pd
import requests
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring

access_key = 'pnWEl7Muj6PpSyrC35SaqRjYnKAAL0xedWtDdUQDmfsWvqDxK1ORAkSg2/axQsJNCKZjQlf98A3TRAuuIzJ0GQ=='
TOTAL_NUM = 75
MAX_TRANSACTION = 30
request_total_num = ( TOTAL_NUM // MAX_TRANSACTION) + 1
target_year = 2020
def xml_to_df(data_root,data_root_name):
    all_data=[]
    column_list = []
    is_column_list = False
    for row in data_root.iter(data_root_name):
        row_data = []
        is_first = True
        for column in row.iter():
            if is_first:
                is_first = False
                continue
            row_data.append(column.text)
            if not is_column_list:
                column_list.append(column.tag)
        is_column_list = True
        all_data.append(row_data)
    return column_list, all_data
def get_request_url(page_no):
    url = 'http://apis.data.go.kr/1480802/iciscsc/csclist'
    params = {'serviceKey': access_key,'numOfRows': MAX_TRANSACTION,'pageNo': page_no, 'yyyy' : target_year}
    response = requests.get(url, params=params)
    return response.text

rename_dict = {'dataNo' : '일련번호', 'cscDe' : '사고일자', 'cscTy' : '사고유형', 'area' : '지역', 'addr' : '주소', 'cause' : '사고원인', 'chem' : '사고물질', 'place' : '발생장소', 'summary' : '사고개요'}
REDEFINE_COLUMNS = ['일련번호', '사고일자', '사고유형', '지역', '주소', '사고원인','사고물질','발생장소','사고개요']
all_data = pd.DataFrame(columns= REDEFINE_COLUMNS)

for page_no in range(1, request_total_num+1):
    raw_xml = get_request_url(page_no)
    root = fromstring(raw_xml)

    data_root = root.find('body').find('items')
    column_list, page_data = xml_to_df(data_root, 'item')

    df = pd.DataFrame(page_data, columns= column_list)
    df.rename(columns=rename_dict, inplace=True)
    # df = df[['기관명', '구분코드', '시도명', '시군구명', '전화번호', '운영가능일자']]
    all_data = pd.concat([all_data, df], ignore_index= True)

print(all_data.shape)

all_data.to_csv('화학사고정보_통합.csv', index = False, encoding= 'cp949')
