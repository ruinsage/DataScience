# 목적: JSON 데이터를 데이터 프레임으로 변환
import json
import requests
import pandas as pd
import cx_Oracle


url = 'http://api.jejuits.go.kr/api/infoRoadEventList'
key = 860553
date = 20230104

def get_request_url(url):
    params = {'code': key}
    response = requests.get(url, params=params)
    return response.text



def get_parsed_json(raw_json):
    all_data = []
    for record in raw_json['info']:
        all_data.append(
        {"ocrr_id": record.get("ocrr_id"),
         "latitude": record.get("latitude"),
         "longitude": record.get("longitude"),
         "heading": record.get("heading"),
         "link_id": record.get("link_id"),
         "code": record.get("code")
         }
        )
    return all_data

def json_to_df_info(raw_json):
    all_data = []
    column_list = ["ocrr_id", "latitude", "longitude","heading","link_id","code"]

    for record in raw_json['info']:
        all_data.append(
            {"ocrr_id": record.get("ocrr_id"),
             "latitude": record.get("latitude"),
             "longitude": record.get("longitude"),
             "heading": record.get("heading"),
             "link_id": record.get("link_id"),
             "code": record.get("code")
             }
        )
    return column_list, all_data

def preprocessed_df_to_oracle(df):
    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    sql_insert = '''
            insert into danger_situation(ocrr_id,latitude,longitude,heading,link_id,code)
            values(:ocrr_id, :latitude, :longitude, :heading, :link_id, :code )
            '''
    for i in range(len(df)-1):
        ocrr_id = df.iloc[i]['ocrr_id']
        latitude = df.iloc[i]['latitude']  # int 값에 대해서는 int 형으로 변환해줘야 한다.
        longitude = df.iloc[i]['longitude']
        heading = df.iloc[i]['heading']
        link_id = df.iloc[i]['link_id']
        code = df.iloc[i]['code']
        cur.execute(sql_insert,
                (ocrr_id,latitude,longitude,heading,link_id,code)
                )

    con.commit()
    cur.close()
    con.close()


# def parking_area_info_collector():
#
#     raw_str_json = get_request_url()
#
#     if raw_str_json:
#         raw_json = json.loads(raw_str_json)
#
#     column_list, all_data = json_to_df_info(raw_json)
#
#     df = pd.DataFrame(all_data, columns=column_list)
#     preprocessed_df_to_oracle(df)




raw_json = get_request_url()

if raw_json:
    raw_json = json.loads(raw_json)

column_list, all_data = json_to_df_info(raw_json)

df = pd.DataFrame(all_data, columns= column_list)

# parking_area_info_collector()

file_name = f'제주도_전기차충전소_자료.csv'
df.to_csv(file_name,index=False,encoding='cp949')

# file_name = f'디지털도서관_자료.json'
#
# with open(file_name, 'w', encoding= 'utf-8') as outfile:
#     retJson = json.dumps(parsed_json, indent=4, sort_keys=True, ensure_ascii = False)
#     outfile.write(retJson)
# print(f'{file_name} saved\n')