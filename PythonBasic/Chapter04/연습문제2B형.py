import random
len_list = int(input("vector 수 : "))
list = []
for i in range(0,len_list) :
    r = random.randint(1, 10)
    list.append(r)
    print(list[i])

serch = int(input("찾을 값을 입력하세요"))
if serch in list :
    print("YES")
else:
    print("NO")