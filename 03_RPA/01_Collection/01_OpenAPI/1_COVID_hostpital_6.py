# 목적: 열 이름 해석 및 순서 정렬

# 열의 의미
#  {'adtFrDd' : '운영가능일자', 'sgguNm' : '시군구명',  'sidoNm' : '시도명', 'spclAdmTyCd' : '구분코드',  'telno' : '전화번호', 'yadmNm' : '기관명'}
#
# * 열의 순서 변경
# ['기관명', '구분코드', '시도명', '시군구명', '전화번호', '운영가능일자']

import pandas as pd

file_name = '코로나19관련_병원정보_응답.csv'

df = pd.read_csv(file_name)
print(f'분석전')
print(df)
print(df.columns)

rename_dict = {'adtFrDd' : '운영가능일자', 'sgguNm' : '시군구명',  'sidoNm' : '시도명', 'spclAdmTyCd' : '구분코드',  'telno' : '전화번호', 'yadmNm' : '기관명'}
df.rename(columns = rename_dict, inplace= True)
df = df[['기관명', '구분코드', '시도명', '시군구명', '전화번호', '운영가능일자']]

print('분석후')
print(df)
