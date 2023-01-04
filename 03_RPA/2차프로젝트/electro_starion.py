# 목적: JSON 데이터를 데이터 프레임으로 변환
import json
import requests
import pandas as pd
import cx_Oracle

def get_request_url():
    url = 'http://api.jejuits.go.kr/api/infoEvInfoList?code=860553'

    response = requests.get(url)
    return response.text

def get_parsed_json(raw_json):
    all_data = []
    for record in raw_json['info']:
        all_data.append(
        {"id": record.get("id"),
         "cid": record.get("cid"),
         "name": record.get("name"),
         "addr": record.get("addr"),
         "use_time": record.get("use_time"),
         "free": record.get("free"),
         "b_name": record.get("b_name"),
         "b_call": record.get("b_call"),
         "type": record.get("type"),
         "x_crdn": record.get("x_crdn"),
         "y_crdn": record.get("y_crdn")}
        )
    return all_data

def json_to_df_info(raw_json):
    all_data = []
    column_list = ["id", "cid", "name","addr","use_time","free","b_name","b_call","type","x_crdn","y_crdn"]

    for record in raw_json['info']:
        all_data.append(
            {"id": record.get("id"),
             "cid": record.get("cid"),
             "name": record.get("name"),
             "addr": record.get("addr"),
             "use_time": record.get("use_time"),
             "free": record.get("free"),
             "b_name": record.get("b_name"),
             "b_call": record.get("b_call"),
             "type": record.get("type"),
             "x_crdn": record.get("x_crdn"),
             "y_crdn": record.get("y_crdn")}
        )
    return column_list, all_data

# def preprocessed_df_to_oracle(df):
#     con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
#     cur = con.cursor()
#     sql_insert = '''
#             insert into bus_753(정류소ID,정류소명,첫번째도착정보메시지,두번째도착정보메시지,제공시각)
#             values(:정류소ID, :정류소명, :첫번째도착정보메시지, :두번째도착정보메시지, :제공시각)
#             '''
#     for i in range(len(df)-1):
#         정류소ID = df.iloc[i]['정류소ID']
#         정류소명 = df.iloc[i]['정류소명']  # int 값에 대해서는 int 형으로 변환해줘야 한다.
#         첫번째도착정보메시지 = df.iloc[i]['첫번째도착정보메시지']
#         두번째도착정보메시지 = df.iloc[i]['두번째도착정보메시지']
#         제공시각 = df.iloc[i]['제공시각']
#         cur.execute(sql_insert,
#                 (정류소ID,정류소명,첫번째도착정보메시지,두번째도착정보메시지,제공시각 )
#                 )
#
#     con.commit()
#     cur.close()
#     con.close()


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