students = [70,60,55,75,95,90,80,80,85,100]
avg = 0
totalsum = 0

for score in students:
    totalsum += score

avg =int (totalsum / len(students))

print(avg)
