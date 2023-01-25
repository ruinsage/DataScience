import pandas as pd
from statsmodels.formula.api import ols
import operator
from itertools import combinations
from datetime import datetime
import time
import seaborn as sns

start = datetime.fromtimestamp(time.time())
print("결과 예측하기")

ground = pd.read_csv('ground.csv', sep=',', header=0, encoding= 'cp949')
ground2 = pd.read_csv('2022 표준지 공시지가.csv', sep=',', header=0)
ground = pd.concat([ground, ground2['공시지가']], axis= 1)
ground.head()
#Boston_house.columns = Boston_house.columns.str.replace(' ', '_')  #열 이름에 공백이 있을 경우 공백을 언더바로 바꾸는데 사용하는 코드

delta = 0.2 # 마진 비율의 값은 데이터/조직의 예측 목표에 따라 조절할 수 있다.
match_dict = {}
columns_list = ['시도명','시군구명','지목','면적','용도지역1','용도지역2','이용상황','주위환경','지세명','형상명','도로교통','방위','지리적위치1_2','지리적위치2_2']

for num in range(1,len(columns_list)+1):
    combi_list = list(combinations(columns_list, num))
    #print(combi_list)
    for tup in combi_list:
        my_formula = '공시지가 ~ '
        for data in tup:
            my_formula += '%s + '%data
        my_formula = my_formula.strip().rstrip('+')
        lm = ols(my_formula, data = ground).fit()
        dependent_variable = ground['공시지가']
        independent_variable = ground[list(tup)] # formula에 들어간 columns만 골라서 고정 변수로 줌
        y_predicted = lm.predict(independent_variable)
        match_count = 0
        for index in range(len(y_predicted)):
            # | 예측값-실제값 | <= 차이를 절대값을 구한다.
            diff = abs(y_predicted[index] - dependent_variable.values[index])

            if (diff / dependent_variable.values[index]) < delta:
                match_count += 1
        print('\n>>'+my_formula.replace('공시지가 ~ ',''))
        print('>> match count = ', match_count)
        print('>> 정답률: %.3f %%'%(match_count/len(y_predicted)*100))
        match_dict['%s'%my_formula.replace('공시지가 ~ ','')] = match_count/len(y_predicted)*100

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