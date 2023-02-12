
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import codecs
import pickle
from konlpy.tag import Okt # Okt : 널리사용되는 형태소 분석기
from gensim.models import word2vec
import pandas as pd
import csv


def back_ground(file_name):
    df = pd.read_csv(file_name, encoding='utf8')
    all_data = []

    for id in df['콘텐츠_ID'].unique():
        row = []
        row.append(id)
        content_list = ''
        flag_first = True
        for content in df['contents'].loc[df['콘텐츠_ID'] == id]:
            if flag_first == True:
                if len(content) > 1:
                    content_list = content
                    flag_first = False
            else:
                if len(content) > 1:
                    content_list = content_list + '\n' + content
        row.append(content_list)
        all_data.append(row)
    return all_data

def make_all_key(all_data):
    all_keys = []
    word_dic = {}
    okt = Okt()
    for index in range(len(all_data)):
        lines = all_data[index][1].split("\n")
        for line in lines:
            malist = okt.pos(line, norm=True, stem=True)
            for word in malist:
                if word[1] == "Noun":  # 명사 확인하기 --- (※3)
                    if len(word[0]) > 1:
                        if not (word[0] in word_dic):
                            word_dic[word[0]] = 0
                        word_dic[word[0]] += 1  # 카운트하기
        # 많이 사용된 명사 출력하기 --- (※4)
        keys = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
        all_keys.append(keys)
    return all_keys

def search_keyword_index(key_word,all_keys):
    max_all_keys = 0
    for num in range(len(all_keys)):
        keys = all_keys[num]
        for index, key in enumerate(keys):
            if key[0] == key_word:
                if max_all_keys < all_keys[num][index][1]:
                    max_all_keys = all_keys[num][index][1]
                    key_index1 = num
                    key_index2 = index
                else:
                    pass
            else:
                pass
    return key_index1

def frequency_store(all_data):
    okt = Okt()
    results = []
    rest_id_list = []
    for id, text in enumerate(all_data):
        lines = text[1].split("\n")
        rest_id_list.append(text[0])
        rl = ''
        r = ''
        for line in lines:
            malist = okt.pos(line, norm=True, stem=True)
            word_list = ''
            for word in malist:
                if not word[1] in ["Josa", "Eomi", "Punctuation"]:
                    word_list = word_list + ' ' + word[0]
            r = r + word_list
        rl = rl + r
        results.append(rl)
    return results,rest_id_list

def similar_store(rest_id,n_recommand,rest_id_list):
    stopwords = ['이다', '이네', '이라고', '이나', '인가', '이고', '싶다', '으로', '인데', '에는',
                 '하다', '하고', '에서', '비다', '알다', '라고', '달다', '다시다', '지만', '에서는']
    vectorizer = TfidfVectorizer(min_df=2, stop_words=stopwords)
    X = vectorizer.fit_transform(results)
    rest_sim = cosine_similarity(X)
    rest_index = rest_id
    recommended_store = []
    similar_rest = sorted(list(enumerate(rest_sim[rest_index])), key=lambda x: x[1], reverse=True)

    for rest_info in similar_rest[0:n_recommand]:
        rest_title = rest_id_list[rest_info[0]]
        recommended_store.append(rest_title)
    return (recommended_store)

def code_to_name(cate_file,result):
    df_cate = pd.read_csv(cate_file , encoding='cp949')
    result2 = []
    for code in result:
        store_index = df_cate.loc[df_cate['콘텐츠 ID'] == code].index
        store_name = df_cate.iloc[store_index]['콘텐츠명'].values[0]
        result2.append(store_name)
    return result2

file_name = 'visit_tourist_review_pre.csv'
cate_file = '관광지end.csv'
n_recommand = 5
all_data = back_ground(file_name)
all_keys = make_all_key(all_data)
results, rest_id_list = frequency_store(all_data)

while True:
    key_word = input("검색어를 입력하세요.")
    key_index = search_keyword_index(key_word,all_keys)
    result = similar_store(key_index,n_recommand,rest_id_list)
    print(result)
    result2 = code_to_name(cate_file,result)
    print(result2)
