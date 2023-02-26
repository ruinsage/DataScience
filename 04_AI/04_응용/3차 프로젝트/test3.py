from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import codecs
import pickle
from konlpy.tag import Okt # Okt : 널리사용되는 형태소 분석기
from gensim.models import word2vec
import pandas as pd
import csv



df = pd.read_csv('관광지end.csv', encoding='CP949')
df['관련 태그 전체'] = df['관련 태그 전체'].str.replace("4.3", "제주4.3")
df['태그'] = df['태그'].str.replace("4.3", "제주4.3")
#df['contents'] = df['contents'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣|\\n ]", "")
sr3 = df['관련 태그 전체'] + ',' + df['태그']

result = []
for tags in sr3:
    data = tags.split(',')
    row = ''
    for tag in data:
        if not (tag in row):
            row = row + ',' + tag
    result.append(row)
print(result)
print(len(result))

