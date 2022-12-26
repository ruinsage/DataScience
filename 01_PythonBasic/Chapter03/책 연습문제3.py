progression = []
sum = 0
for i in range(1,101):
    if i%3 == 0 :
        if i%2 != 0 :
            progression.append(i)
            sum += i

print(progression)
print(sum)
