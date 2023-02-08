from flask import Flask
# pip install flask-restful
from flask_restful import Resource, Api
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import codecs
import pickle
from konlpy.tag import Okt # Okt : 널리사용되는 형태소 분석기
from gensim.models import word2vec
import pandas as pd
import csv

app = Flask(__name__)
app.debug = True
api = Api(app)

class CreateUser(Resource):
    def get(self):
        return {'status': 'success user'}
api.add_resource(CreateUser, '/user')

class CreateUser2(Resource):
    def get(self):
        return {'status': 'success user2'}
api.add_resource(CreateUser2, '/user2')

class Multi(Resource):
    def get(self,num):
        return {'result':num*10}

api.add_resource(Multi,'/multi/<int:num>')
if __name__ == '__main__':
    app.run(host='localhost')
    # app.run(host='192.168.0.161')
