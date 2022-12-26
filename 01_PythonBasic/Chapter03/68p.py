import random

# 2. 이름 list에 전체 이름, 특정 이름 출력
names = ['홍길동','이순신','유관순']
print(names) # 전체 이름
print(names[2]) # , 특정 이름 출력

if '유관순' in names:
    print('유관순 있음')
else:
    print('유관순 없음')

idx = random.randint (0,2)
print(f'idx : {idx}')
print(names[idx])

idx = random.randint (0,10)
names = ['김유진','문성준','박종민','송지예','양석훈','이예지','임성형','한권제','현재봉','김지혜','이현구']
print(f" 축하합니다. {names[idx]}씨 전원 아이스크림 쏘세요")