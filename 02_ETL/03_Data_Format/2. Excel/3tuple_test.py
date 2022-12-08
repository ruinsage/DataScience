from datetime import date
my_date = (2013, 1, 1, 0, 0, 0)

print(my_date)

print(my_date[0:3])
print(*my_date[0:3])
# *을 붙인 문자열은 튜플이 아니라 문자열 자체로 출력된다
date_cell = date(*my_date[0:3]).strftime\
	('%m/%d/%Y')
print(date_cell)
print("End")