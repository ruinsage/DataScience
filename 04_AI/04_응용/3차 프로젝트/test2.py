from konlpy.tag import Okt # Okt : 널리사용되는 형태소 분석기
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def keyword_pre(key_word):
    okt = Okt()
    results = []
    malist = okt.pos(key_word, norm=True, stem=True)
    for word in malist:
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            results.append(word[0])
    return results

def search_keyword_index(key_word,all_keys):
    sum_keyword_place = 0
    for num in range(len(all_keys)): # 업체별
        max_value = 0
        keys = all_keys[num]
        for word in key_word: # 키워드 단어별
            tuple_count = 0
            for index, key in enumerate(keys): # 튜플 별
                check_point = 0
                if key[0] == word: # 키워드 단어와 일치하면
                    if tuple_count < all_keys[num][index][1]: # 최대값이 빈도수보다 낮으면
                        check_point = all_keys[num][index][1]
                        tuple_count = tuple_count + check_point
                        max_value = tuple_count + max_value
                        if sum_keyword_place < max_value:
                            target_index = num
        if sum_keyword_place < max_value:
            sum_keyword_place = max_value
    print(sum_keyword_place)
    print(target_index)
    return target_index

def similar_store(rest_id,n_recommand,rest_id_list):
    recommended_store = []

    # # 후기 기준 유사업체
    rest_index = rest_id
    similar_rest = sorted(list(enumerate(tour_sim[rest_index])), key=lambda x: x[1], reverse=True)

    for rest_info in similar_rest[0:n_recommand//2]:
        print(f'후기 기반 코사인 유사도 : {rest_info}')
        rest_title = rest_id_list[rest_info[0]]
        recommended_store.append(rest_title)

    # 소개글 기준 유사업체
    similar_rest2 = sorted(list(enumerate(tour_sim2[rest_index])), key=lambda x: x[1], reverse=True)
    while True:
        if len(recommended_store) >= n_recommand:
            break
        else:
            for rest_info2 in similar_rest2[1:]:
                rest_title = rest_id_list[rest_info2[0]]
                print(f'소개글 기반 코사인 유사도 : {rest_info}')
                if not (rest_title in recommended_store):
                    recommended_store.append(rest_title)
                    if len(recommended_store) >= n_recommand:
                        break

    return (recommended_store)

def code_to_name(cate_file,result):
    df_cate = pd.read_csv(cate_file , encoding='cp949')
    result2 = []
    for code in result:
        store_index = df_cate.loc[df_cate['콘텐츠 ID'] == code].index
        store_name = df_cate.iloc[store_index]['콘텐츠명'].values[0]
        result2.append(store_name)
    return result2


with open("tour_sim.pickle","rb") as fr:
    tour_sim = pickle.load(fr)
with open("id_list.pickle","rb") as fr:
    rest_id_list = pickle.load(fr)
with open("tour_sim2.pickle","rb") as fr:
    tour_sim2 = pickle.load(fr)
with open("all_keys.pickle","rb") as fr:
    all_keys = pickle.load(fr)

n_recommand = 10
file_name = 'visit_tourist_review_pre.csv'
cate_file = '관광지end.csv'

key_word = '바다에서온천 수영'
#key_word = '꽃마차'
key_word2 = keyword_pre(key_word)
print(key_word2)
key_index = search_keyword_index(key_word2, all_keys)
result = similar_store(key_index, n_recommand, rest_id_list)
print(result)
result2 = code_to_name(cate_file, result)
print(result2)