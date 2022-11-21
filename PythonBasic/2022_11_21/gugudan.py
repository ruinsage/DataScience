def gugu(dan):
    for num in range(1,10):
        print(f"{int(dan) * num}\t",end='')

def all_gugu():
    for num2 in range(2,10):
        gugu(num2)
        print()


select = input("원하는 단을 입력하세요(예: 2 , 전체: all)")

if select == 'all' :
    all_gugu()
else:
    gugu(select)


