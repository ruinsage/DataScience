point = {'kim99' : 12000,
         'lee66' : 11000,
         'han55' : 3000,
         'hong77' : 5000,
         'hwang33' : 18000}

score = []

for i in point :
    score.append(point[i])

hight = max(score)

for id in point :
    point[id] = hight

print(f"{id}님의 {hight}점이 가장 높은 점수입니다")



