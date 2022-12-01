index_list = []
def make_index(n):
    for month in range(1,n+1):
        for week in range(1,n+1):
            index = str(month) + '월' + str(week) + '주'
            index_list.append(index)

make_index(4)
print(index_list)
