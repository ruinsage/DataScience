# 목적:  JSON parsing
import json

import requests
# Encoding key
# access_key = 'pnWEl7Muj6PpSyrC35SaqRjYnKAAL0xedWtDdUQDmfsWvqDxK1ORAkSg2%2FaxQsJNCKZjQlf98A3TRAuuIzJ0GQ%3D%3D'
# Decoding key

def get_request_url():
    url = 'http://library.me.go.kr/pyxis-api/2/collections/2/search?all=k|a|library'

    response = requests.get(url)
    # response.content # => response.content는 한글이 인코딩된 형식이므로
    #                       response.text를 응답받기로 함
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

raw_json = get_request_url()

if raw_json:
    raw_json = json.loads(raw_json)
parsed_json = get_parsed_json(raw_json)
print(parsed_json)
