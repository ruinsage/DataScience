import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations
from datetime import datetime
import time

start = datetime.fromtimestamp(time.time())
print("결과 예측하기")
Boston_house = pd.read_csv('Boston_house.csv', sep = ',', header= 0)
#Boston_house.columns = Boston_house.columns.str.replace(' ', '_')  #열 이름에 공백이 있을 경우 공백을 언더바로 바꾸는데 사용하는 코드

match_dict = {}
columns_list = ['AGE','B','RM','CRIM','DIS','INDUS','LSTAT','NOX','PTRATIO','RAD','ZN','TAX','CHAS']

for num in range(1,14):
    combi_list = list(combinations(columns_list, num))
    #print(combi_list)
    for tup in combi_list:
        my_formula = 'Target ~ '
        for data in tup:
            my_formula += '%s + '%data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data = Boston_house).fit()
        dependent_variable = Boston_house['Target']
        independent_variable = Boston_house[list(tup)] # formula에 들어간 columns만 골라서 고정 변수로 줌
        y_predicted = lm.predict(independent_variable)
        y_predicted_rounded = [round(score) for score in y_predicted]
        match_count = 0
        for index in range(len(y_predicted_rounded)):
            if y_predicted_rounded[index] == dependent_variable.values[index]:
                match_count += 1
        print('\n>>'+my_formula.replace('Target ~ ',''))
        print('>> match count = ', match_count)
        print('>> 정답률: %.3f %%'%(match_count/len(y_predicted_rounded)*100))
        match_dict['%s'%my_formula.replace('Target ~ ','')] = match_count/len(y_predicted_rounded)*100

# 최대값 찾기
match_dic = sorted(match_dict.items(), key = operator.itemgetter(1), reverse= True)
#print(match_dic)

print("\n\n 독립변수 최적화 분석 결과")
print('총 조합 갯수: %d'%len(match_dic))
print('MAX 조합: %s >> %.3f %%'%(match_dic[0][0],match_dic[0][1]))
end = datetime.fromtimestamp(time.time())
print(f'분석 시작: {start}')
print(f'분석 종료: {end}')
print(f'총 분석 시간: {end - start}')