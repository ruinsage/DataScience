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
#house.columns = house.columns.str.replace(' ','_')
#change_list = ['driveway','recroom','fullbase','gashw','airco','garagepl','prefarea']
house.driveway = house.driveway.replace('no',0)
house.driveway = house.driveway.replace('yes', 1)
house.recroom = house.recroom.replace('no',0)
house.recroom = house.recroom.replace('yes', 1)
house.fullbase = house.fullbase.replace('no',0)
house.fullbase = house.fullbase.replace('yes', 1)
house.gashw = house.gashw.replace('no',0)
house.gashw = house.gashw.replace('yes', 1)
house.airco = house.airco.replace('no',0)
house.airco = house.airco.replace('yes', 1)
house.garagepl = house.garagepl.replace('no',0)
house.garagepl = house.garagepl.replace('yes', 1)
house.prefarea = house.prefarea.replace('no',0)
house.prefarea = house.prefarea.replace('yes', 1)
house.price =house.price/10000
#house.lotsize = round(house.lotsize,)
print(house)

match_dic={}
colums_list = ['lotsize','bedrooms','bathrms','stories','driveway','recroom','fullbase','gashw','airco','garagepl','prefarea']

for num in range(1,len(colums_list)+1):
    combi_list = list(combinations(colums_list,num))
    for tup in combi_list:
        my_formula = 'price ~ '
        for data in tup:
            my_formula+='%s + '%data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data=house).fit()
        dependent_variable = house['price']
        independent_variables = house[list(tup)] # formula 에 들어간 columns만 골라서 고정 변수로 줌
        independent_variables_standardized = (independent_variables - independent_variables.mean()) / independent_variables.std()
        y_predicted = lm.predict(independent_variables)
        y_predicted_rounded = [round(score) for score in y_predicted]

        for index, score in enumerate(y_predicted_rounded): # enumerate를 이용하여 index와 score를 꺼낸다
            if len(str(score)) > 1: # score의 자릿수가 2자리 이상이라면(3자리라면)
                y_predicted_rounded[index] = round(score,-1 ) # 해당 스코어의 일의 자리에서 반올림
            else:
                y_predicted_rounded[index] = round(score)

        match_count=0
        for index in range(len(y_predicted_rounded)):
            target_price = 0
            if len(str(round(dependent_variable.values[index]))) == 2: # 만약 종속변수 값이 2자리라면
                target_price = round(dependent_variable.values[index],-1) # 해당 종속변수 값의 일의 자리에서 반올림
            else:   # 만약 종속변수 값이 2자리가 아니라면
                target_price = round(dependent_variable.values[index]) # 해당 종속변수 값의 일의 자리에서 반올림
            if y_predicted_rounded[index] == target_price:
                match_count+=1
        print('\n>> '+my_formula.replace('price ~ ',''))
        print('>> match count=',match_count)
        print('>> 정답률: %.2f %%'%(match_count/len(y_predicted_rounded)*100))
        match_dic['%s'%my_formula.replace('price ~ ','')] = match_count/len(y_predicted_rounded)*100


# 최대값 찾기
match_dic = sorted(match_dic.items(), key=operator.itemgetter(1),reverse=True)
#print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d'%len(match_dic))
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0],match_dic[0][1]))
end = datetime.fromtimestamp(time.time())
print(f'분석 시작: {start}')
print(f'분석 종료: {end}')
print(f'총 분석 시간: {end-start}')