
for num in range(1,101):
    print(num)

numbers = result = 0

while numbers <= 1000:
    numbers += 1
    if numbers %3 == 0 :
        result += numbers
print(result)

student = [70,60,55,75,95,90,80,80,85,100]
sum2 = 0
for score in student:
    sum2 += score

avg = sum2 / len(student)
print(f"평균점수: {avg}")

for star in range(1,6):
    print('*' * star)

max_blank = 5
star = 1

while max_blank > 0:
    print(' ' * max_blank,end=' ')
    max_blank -= 1
    print('*' * star)
    star += 1

max_blank = 5
for star in range(1,6):
    print(' ' * max_blank,end=' ')
    print('*' * star)
    max_blank -= 1



