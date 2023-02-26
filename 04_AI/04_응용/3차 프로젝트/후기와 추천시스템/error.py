from flask_restful import Resource, Api
import pickle
from konlpy.tag import Okt # Okt : 널리사용되는 형태소 분석기
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from random import randrange

app = Flask(__name__)
CORS(app)
CORS(app, resources={r'*': {'origins': 'https://localhost:9090'}})
app.config['JSON_AS_ASCII'] = False
app.debug = True
api = Api(app)

with open("id_list.pickle","rb") as fr:
    id_list = pickle.load(fr)
with open("tour_sim2.pickle","rb") as fr:
    tour_sim = pickle.load(fr)

content_df = pd.read_csv('tourplace_info.csv', encoding='cp949')

def get_recommended_content_code(content_index, content_id_list):
    recommended_content_code = []
    similar_content_code_list = sorted(list(enumerate(tour_sim[content_index])), key=lambda x: x[1], reverse=True)

    for i in range(5) :
        idx = similar_content_code_list[i][0]
        recommended_content_code.append(content_id_list[idx])

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
    result_index = []
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
    if len(index_list) == 0:
        index_list.append(-1)
        result_index = index_list
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
            result_code = get_recommended_content_code(place_index, id_list)
            print(result_code)
            data = {
                'titleList' : code_to_title(result_code),
                'idList' : result_code
            }

            return jsonify(data)

api.add_resource(CreateKeyword,'/code/<string:code>')

if __name__ == '__main__':
    app.run(host='localhost', debug=False)