import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations
from datetime import datetime
import time
import math

start = datetime.fromtimestamp(time.time())
print("결과 예측하기")
house = pd.read_csv('Housing.csv',sep=',',header=0)
house.price =house.price/10000
print(house)
print(round(max(house.price),-1))
print(round(min(house.price)))