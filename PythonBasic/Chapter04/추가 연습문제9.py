temperature = {'월':25.5,
               '화':28.3,
               '수':33.2,
               '목':32.1,
               '금':17.3,
               '토':35.3,
               '일':33.3}
word_num = 54
print("-" * word_num)

for day in temperature :
    print(f"  {day}\t",end = '')

print()
print("-" * word_num)

for day in temperature :
    print(f" {temperature[day]}\t",end = '')

print()
print("-" * word_num)