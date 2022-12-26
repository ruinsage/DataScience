import random

list = []  #변수 초기화

for i in range (10): # 0~9
    r = random.randint (1,10)
    list.append(r)

print(f'list = {list}')

for i in range (10):
    print(list[i] * 0.25)
