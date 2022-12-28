# 목적: JSON 데이터를 데이터 프레임으로 변환
import json
import requests
import pandas as pd

def get_request_url():
    url = 'http://library.me.go.kr/pyxis-api/2/collections/2/search?all=k|a|library'

    response = requests.get(url)
    return response.text

def get_parsed_json(raw_json):
    all_data = []
    for record in raw_json['data']['list']:
        all_data.append(
        {"id": record.get("id"),
         "biblioType": record.get("biblioType"),
         "thumbnailUrl": record.get("thumbnailUrl"),
         "isbn": record.get("isbn"),
         "issn": record.get("issn"),
         "titleStatement": record.get("titleStatement"),
         "author": record.get("author"),
         "publication": record.get("publication"),
         "etcContent": record.get("etcContent"),
         "branchVolumes": record.get("branchVolumes"),
         "erSources": record.get("erSources"),
         "resources": record.get("resources"),
         "newResources": record.get("newResources"),
         "similars": record.get("similars")}
        )
    return all_data

def json_to_df_info(raw_json):
    all_data = []
    column_list = ['id','biblioType','thumbnailUrl','isbn','issn','titleStatement','author','publication','etcContent','branchVolumes','erSources','resources','newResources','similars']

    for record in raw_json['data']['list']:
        all_data.append(
            {"id": record.get("id"),
             "biblioType": record.get("biblioType"),
             "thumbnailUrl": record.get("thumbnailUrl"),
             "isbn": record.get("isbn"),
             "issn": record.get("issn"),
             "titleStatement": record.get("titleStatement"),
             "author": record.get("author"),
             "publication": record.get("publication"),
             "etcContent": record.get("etcContent"),
             "branchVolumes": record.get("branchVolumes"),
             "erSources": record.get("erSources"),
             "resources": record.get("resources"),
             "newResources": record.get("newResources"),
             "similars": record.get("similars")}
        )
    return column_list, all_data


raw_json = get_request_url()

if raw_json:
    raw_json = json.loads(raw_json)

column_list, all_data = json_to_df_info(raw_json)

df = pd.DataFrame(all_data, columns= column_list)

file_name = f'디지털도서관_자료.csv'
df.to_csv(file_name,index=False,encoding='cp949')

# file_name = f'디지털도서관_자료.json'
#
# with open(file_name, 'w', encoding= 'utf-8') as outfile:
#     retJson = json.dumps(parsed_json, indent=4, sort_keys=True, ensure_ascii = False)
#     outfile.write(retJson)
# print(f'{file_name} saved\n')