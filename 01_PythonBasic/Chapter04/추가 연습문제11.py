temperature = {'월':25.5,
               '화':28.3,
               '수':33.2,
               '목':32.1,
               '금':17.3,
               '토':35.3,
               '일':33.3}
list = []
for day in temperature :
    if temperature[day] >= 30 :
        list.append(day)

#print(list)
#len 사용해서 마지막 원소 찾아볼 것
#print(len(list))

for day in list:
    if day == list[len(list) - 1] :
        print(day,end=' ')
    else :
       print(day,end=', ')

#print(f"{', '.join(list)}") #솔루션 방법
