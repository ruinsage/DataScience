from flask_restful import Resource, Api
import pickle
from flask import Flask, jsonify
from flask_cors import CORS
from random import randrange
import time
import cx_Oracle
import pandas as pd


app = Flask(__name__)
CORS(app)
CORS(app, resources={r'*': {'origins': 'https://192.168.0.161:9090'}})
app.config['JSON_AS_ASCII'] = False
app.debug = True
api = Api(app)

with open("id_list.pickle","rb") as fr:
    id_list = pickle.load(fr)
with open("tour_sim2.pickle","rb") as fr:
    tour_sim = pickle.load(fr)

content_df = pd.read_csv('tourplace_info.csv', encoding='cp949')

def make_herricane_df(shhet_name) :
    input_file = 'herricane.xlsx'
    RoadWork_df = pd.read_excel(input_file, sheet_name=shhet_name)
    print(RoadWork_df)
    return RoadWork_df

def hericane_RoadWork_to_oracle(RoadWork) :
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    query = 'merge into ROAD_WORK ' \
            'using DUAL on (id = :ocrr_id) ' \
            'when matched then ' \
            'update set last_updated_at = :current_time ' \
            'when not matched then ' \
            'insert (id, lat, lon, heading, link_id, whole_lane, block_lane, text, created_at, last_updated_at) ' \
            'values (:ocrr_id, :lat, :lon, :heading, :link_id, :whole_lane, :block_lane, :text, :current_time, :current_time)'

    for i in range(len(RoadWork)):
        ocrr_id = int(RoadWork.iloc[i]['ocrr_id'])
        lat = float(RoadWork.iloc[i]['latitude'])
        lon = float(RoadWork.iloc[i]['longitude'])
        heading = int(RoadWork.iloc[i]['heading'])
        link_id = int(RoadWork.iloc[i]['link_id'])
        whole_lane = int(RoadWork.iloc[i]['whole_lane'])
        block_lane = int(RoadWork.iloc[i]['block_lane'])
        text = RoadWork.iloc[i]['text']

        cur.execute(query, (ocrr_id, current_time, ocrr_id, lat, lon, heading, link_id, whole_lane, block_lane, text, current_time, current_time))

    con.commit()
    cur.close()
    con.close()

def hericane_ROADEVENT_to_oracle(ROADEVENT_df) :
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    query = 'merge into ROAD_EVENT ' \
            'using DUAL on (id = :ocrr_id) ' \
            'when matched then ' \
            'update set last_updated_at = :current_time ' \
            'when not matched then ' \
            'insert (id, lat, lon, heading, link_id, code, created_at, last_updated_at) ' \
            'values (:ocrr_id, :lat, :lon, :heading, :link_id, :code, :current_time, :current_time)'

    for i in range(len(ROADEVENT_df)):
        ocrr_id = ROADEVENT_df.iloc[i]["ocrr_id"]
        lat = float(ROADEVENT_df.iloc[i]["latitude"])
        lon = float(ROADEVENT_df.iloc[i]["longitude"])
        heading = int(ROADEVENT_df.iloc[i]["heading"])
        link_id = int(ROADEVENT_df.iloc[i]["link_id"])
        code = int(ROADEVENT_df.iloc[i]["code"])

        cur.execute(query, (ocrr_id, current_time, ocrr_id, lat, lon, heading, link_id, code, current_time, current_time))

    con.commit()
    cur.close()
    con.close()

def hericane_RoadCondition_to_oracle(RoadCondition_df) :
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    query = 'insert into ROAD_CONDITION values (ROAD_CONDITION_SEQ.NEXTVAL, :lat, :lon, :heading, :link_id, :visibility, :snow, :road_temp, :water_film, :friction, :code, :current_time)'


    for i in range(len(RoadCondition_df)):
        lat = float(RoadCondition_df.iloc[i]["latitude"])
        lon = float(RoadCondition_df.iloc[i]["longitude"])
        heading = int(RoadCondition_df.iloc[i]["heading"])
        link_id = int(RoadCondition_df.iloc[i]["link_id"])
        visibility = int(RoadCondition_df.iloc[i]["visibility"])
        snow = int(RoadCondition_df.iloc[i]["snow"])
        road_temp = float(RoadCondition_df.iloc[i]["road_temp"])
        water_film = int(RoadCondition_df.iloc[i]["water_film"])
        friction = int(RoadCondition_df.iloc[i]["friction"])
        code = int(RoadCondition_df.iloc[i]["code"])

        cur.execute(query, (lat, lon, heading, link_id, visibility, snow, road_temp, water_film, friction, code, current_time))

    con.commit()
    cur.close()
    con.close()

def hericane_RoadClose_to_oracle(RoadClose_df) :
    RoadClose_df['ocrr_id'] = pd.to_numeric(RoadClose_df['ocrr_id'], errors='coerce')
    RoadClose_df = RoadClose_df.dropna(subset=['ocrr_id'])
    RoadClose_df['ocrr_id'] = RoadClose_df['ocrr_id'].astype(int)
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')

    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    query = 'merge into ROAD_CLOSE ' \
            'using DUAL on (id = :ocrr_id) ' \
            'when matched then ' \
            'update set last_updated_at = :current_time ' \
            'when not matched then ' \
            'insert (id, lat, lon, heading, link_id, whole_lane, block_lane, text, created_at, last_updated_at) ' \
            'values (:ocrr_id, :lat, :lon, :heading, :link_id, :whole_lane, :block_lane, :text, :current_time, :current_time)'

    for i in range(len(RoadClose_df)):
        ocrr_id = int(RoadClose_df.iloc[i]['ocrr_id'])
        lat = float(RoadClose_df.iloc[i]['latitude'])  # int 값에 대해서는 int 형으로 변환해줘야 한다.
        lon = float(RoadClose_df.iloc[i]['longitude'])
        heading = int(RoadClose_df.iloc[i]['heading'])
        link_id = int(RoadClose_df.iloc[i]['link_id'])
        whole_lane = int(RoadClose_df.iloc[i]['whole_lane'])
        block_lane = int(RoadClose_df.iloc[i]['block_lane'])
        text = RoadClose_df.iloc[i]['text']

        cur.execute(query, (ocrr_id, current_time, ocrr_id, lat, lon, heading, link_id, whole_lane, block_lane, text, current_time, current_time))

    con.commit()
    cur.close()
    con.close()

def get_recommended_content_code(content_index, content_id_list):
    recommended_content_code = []
    similar_content_code_list = sorted(list(enumerate(tour_sim[content_index])), key=lambda x: x[1], reverse=True)

    for place_info in similar_content_code_list[1:6]:
        place_title = content_id_list[place_info[0]]
        recommended_content_code.append(place_title)

    return recommended_content_code

def code_to_tag(code):
    code_list = code.split()
    key_tag = []
    if len(code_list) > 0:
        for input_code in code_list: # 코드리스트에서 코드를 하나씩 꺼내어
            tag_data = content_df.loc[content_df['ID'] == input_code]['tags'].values # 해당 장소의 태그 값을 받고
            for tags in tag_data:
                tag_split = tags.split(',')
                for tag in tag_split:
                    if not tag in key_tag:
                        key_tag.append(tag)
    else:
        key_tag.append(-1)
    return key_tag

def search_tag(key_tag):
    index_list = []
    for index,tags in enumerate(content_df['tags']): # 각 장소의 태그 값을 꺼내어
        place_count = 0
        for tag in tags.split(','): # 쉽표로 나눈 각 태그가
            tag_count = 0
            for key in key_tag:     # 키태그리스트에서 키태그를 하나씩 꺼내고
                if tag == key: # 키태그와 같다면
                    tag_count += 1 # 태그 카운트 +1
            place_count += tag_count
        if len(tags.split(',')) == place_count:
            index_list.append(index)
    print(index_list)
    if len(index_list) == 0:
        index_list.append(-1)
        result_index = index_list[0]
    elif len(index_list) == 1:
        result_index = index_list[0]
    else:
        random_num = randrange(1, len(index_list))
        result_index = index_list[random_num]
    return result_index

def code_to_title(code_list):
    title_list = []
    for code in code_list:
        print(code)
        store_index = content_df.loc[content_df['ID'] == code].index
        print(store_index)
        store_name = content_df.iloc[store_index]['name'].values[0]
        title_list.append(store_name)
    return title_list

class CreateKeyword(Resource):
    def get(self, code):

        print(f'code : {code}')
        only_tag = code_to_tag(code)
        #print(f'only_tag : {only_tag}')

        if only_tag == -1:
            print('입력값없음')
            pass
        else:
            place_index = search_tag(only_tag)
            if place_index == -1:
                print('입력값없음')
                pass
            else:
                result_code = get_recommended_content_code(place_index, id_list)
                print(result_code)
                data = {
                    'titleList' : code_to_title(result_code),
                    'idList' : result_code
                }
            return jsonify(data)

class herricane():
    def post(self):
        for i in range(1, 5):
            hericane_ROADEVENT_to_oracle(make_herricane_df(f'ROADEVENT{i}'))
            hericane_RoadWork_to_oracle(make_herricane_df(f'RoadWork{i}'))
            hericane_RoadCondition_to_oracle(make_herricane_df(f'RoadCondition{i}'))
            hericane_RoadClose_to_oracle(make_herricane_df(f'RoadClose{i}'))
            time.sleep(25)

api.add_resource(CreateKeyword,'/code/<string:code>')
api.add_resource(CreateKeyword,'/herricane/')

if __name__ == '__main__':
    app.run(host='192.168.0.161', debug=False)
