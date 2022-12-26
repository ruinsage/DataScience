i = 0
simbol = "*"
simbol2 = " "
backnum = [5,4,3,2,1,0]

for j in backnum:
    print(f"{simbol2*int(j)}", end=' ')
    print(f"{simbol*i}", end =' ')
    i += 1
    print()

