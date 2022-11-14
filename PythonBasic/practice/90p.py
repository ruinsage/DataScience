result = ['문자','문저','만자','몬자','몬쟈']
result.sort()
print(result)

import random
r = []
for i in range(5):
    r.append(random.randint(1,5))

print(r)
if 4 in r:
    print("있음")
else :
    print("없음")