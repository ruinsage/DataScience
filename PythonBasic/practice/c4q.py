list2 = [1,3,4,5,2]
list2.sort()
list2.reverse()
print(list2)

tuple = (1,2,3)
tuple = tuple +(4,)
print(tuple)

a = {'A':90,'B':80,'C':70}

print(a.pop('B'))
print(a)

a = [1,1,1,2,2,3,3,3,4,4,5]

s_a = set(a)
l_a = list(s_a)
print(l_a)

milige = {'kim99':12000,'lee66':11000,'han55':3000,'hong55':5000,'hwang33':18000}

for i in milige:
    print(f"아이디: {i}, 마일리지: {milige[i]}점")

id = 'han55'
milige['han55'] = 5000
for key in milige:
    if key == 'han55':
        print(f"{key}님의 마일리지가 {milige['han55']}점으로 수정되었습니다.")

print(f"{id}님의 마일리지가 {milige.get('han55')}점으로 수정되었씁니다.")