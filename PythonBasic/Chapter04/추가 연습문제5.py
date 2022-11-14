
point = {'kim99' : 12000,
         'lee66' : 11000,
         'han55' : 3000,
         'hong77' : 5000,
         'hwang33' : 18000}
num = 0
for i in point :
    num += 1
    print(f"{num}. 아이디: {i}, 마일리지: {point[i]}점")
