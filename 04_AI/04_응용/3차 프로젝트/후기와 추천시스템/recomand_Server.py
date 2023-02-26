
# pip install flask-restful
from flask_restful import Resource, Api
import pickle
from konlpy.tag import Okt # Okt : 널리사용되는 형태소 분석기
import pandas as pd
import requests
import json
from flask import Flask
from urllib import parse
import urllib
from urllib.parse import quote_plus
from urllib.parse import unquote_plus

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.debug = True
api = Api(app)

class CreateKeyword(Resource):
    def get(self,keyword):
        print(keyword)
        def keyword_pre(key_word):
            okt = Okt()
            results = []
            malist = okt.pos(key_word, norm=True, stem=True)
            for word in malist:
                if not word[1] in ["Josa", "Eomi", "Punctuation"]:
                    results.append(word[0])
            return results

        def search_keyword_index(key_word, all_keys):
            sum_keyword_place = 0
            for num in range(len(all_keys)):  # 업체별
                max_value = 0
                keys = all_keys[num]
                for word in key_word:  # 키워드 단어별
                    tuple_count = 0
                    for index, key in enumerate(keys):  # 튜플 별
                        check_point = 0
                        if key[0] == word:  # 키워드 단어와 일치하면
                            if tuple_count < all_keys[num][index][1]:  # 최대값이 빈도수보다 낮으면
                                check_point = all_keys[num][index][1]
                                tuple_count = tuple_count + check_point
                                max_value = tuple_count + max_value
                if sum_keyword_place < max_value:
                    sum_keyword_place = max_value
                    target_index = num
            if sum_keyword_place == 0:
                target_index = -1
            print(sum_keyword_place)
            return target_index

        def similar_store(rest_id, n_recommand, rest_id_list):
            recommended_store = []
            rest_index = rest_id
            # 태그 4 : 후기 6 유사업체
            tour_sim2 = (tour_sim3 * 0.3) + (tour_sim * 0.7)
            similar_rest2 = sorted(list(enumerate(tour_sim2[rest_index])), key=lambda x: x[1], reverse=True)
            while True:
                if len(recommended_store) >= n_recommand:
                    break
                else:
                    for rest_info2 in similar_rest2[0:]:
                        rest_title = rest_id_list[rest_info2[0]]
                        # print(f'후기 기반 코사인 유사도 : {rest_info2}')
                        if not (rest_title in recommended_store):
                            recommended_store.append(rest_title)
                            if len(recommended_store) >= n_recommand:
                                break

            return (recommended_store)

        def code_to_name( result_code):

            result2 = []
            for code in result_code:
                store_index = df_cate.loc[df_cate['콘텐츠 ID'] == code].index
                store_name = df_cate.iloc[store_index]['콘텐츠명'].values[0]
                result2.append(store_name)
            return result2

        def get_request_url(q, display):
            client_id = '4UxNV6vDfeRgzF0HPUZl'
            client_secret = 'ZMbB7PUnjd'

            encText = urllib.parse.quote(q)  # <- search keyword
            url = "https://openapi.naver.com/v1/search/blog?display="+display+"&query=" + encText  # json 결과
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id", client_id)
            request.add_header("X-Naver-Client-Secret", client_secret)
            response = urllib.request.urlopen(request)
            rescode = response.getcode()

            if (rescode == 200):
                response_body = json.load(response)
                data = []
                for item in response_body['items']:
                    row_data = []
                    row_data.append(item['title'])
                    row_data.append(item['link'])
                    row_data.append(item['description'])
                    data.append(row_data)
            else:
                print("Error Code:" + rescode)
            return data

        def get_request_url2(q):
            key = 'AIzaSyCF4rJYoAoJ135ad6tNAR5qBRncxvR0th8'
            url = 'https://www.googleapis.com/youtube/v3/search'
            params = {'part': 'snippet', 'maxResults': 1, 'type': 'video', 'q': q, 'key': key}
            response = requests.get(url, params=params)
            return response.text

        cate_file = '관광지end.csv'
        n_recommand = 5
        df_cate = pd.read_csv(cate_file, encoding='cp949')

        with open("all_keys.pickle", "rb") as fr:
            all_keys = pickle.load(fr)
        with open("id_list.pickle", "rb") as fr:
            id_list = pickle.load(fr)
        with open("tour_sim.pickle", "rb") as fr:
            tour_sim = pickle.load(fr)
        with open("tour_sim3.pickle", "rb") as fr:
            tour_sim3 = pickle.load(fr)

        while True:
            #key_word = '바다'
            key_word2 = keyword_pre(keyword)
            key_index = search_keyword_index(key_word2, all_keys)
            print(f'키워드인덱스:{key_index}')
            if key_index == -1:
                pass
            else:
                result_code = similar_store(key_index, n_recommand, id_list)
                print(result_code)
                result2 = code_to_name( result_code)
                print(result2)
                m1 = dict(zip(range(1, len(result2) + 1), result2))

                blog_data = []
                for q in result2:
                    data = get_request_url(str(q), "3")
                    print(data)
                    blog_data.append(data)

                m2 = dict(zip(range(1, len(blog_data) + 1), blog_data))

                # for q in result2:
                #     raw_json = json.loads(get_request_url2(q))
                #     # print(raw_json)
                #     youtube_data = []
                #     for item in raw_json['items']:
                #         row = []
                #         print(f"제목 : {item['snippet']['title']}")
                #         row.append(item['snippet']['title'])
                #         print(f"썸네일 : {item['snippet']['thumbnails']['default']['url']}")
                #         row.append(item['snippet']['thumbnails']['default']['url'])
                #         print(f"영상ID : {item['id']['videoId']}")
                #         row.append(item['id']['videoId'])
                #         print(f"URL : https://www.youtube.com/watch?v={item['id']['videoId']}")
                #         row.append(item['id']['videoId'])
                #         youtube_data.append(row)

                # print(blog_data)
                # print(youtube_data)

                # m3 = dict(zip(range(1, len(youtube_data) + 1), youtube_data))

                lst4 = [m1, m2]
                m4 = dict(zip(range(11, len(lst4) + 12), lst4))

                json_str = json.dumps(m4)
                print(json.loads(json_str))
                print('프로그램 종료')
                return m4

with open("all_keys.pickle", "rb") as fr:
    all_keys = pickle.load(fr)
with open("id_list.pickle", "rb") as fr:
    id_list = pickle.load(fr)
with open("tour_sim.pickle", "rb") as fr:
    tour_sim = pickle.load(fr)
with open("tour_sim3.pickle", "rb") as fr:
    tour_sim3 = pickle.load(fr)
api.add_resource(CreateKeyword,'/keyword/<string:keyword>')

if __name__ == '__main__':
    #app.run(host='localhost')
    app.run(host='192.168.0.161')

