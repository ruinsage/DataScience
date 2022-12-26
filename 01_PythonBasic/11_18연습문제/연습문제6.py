def gugu(dan):
    for num in range(1,10):
        result = int(dan) * num
        print(result,end='\t')
def all_gugu(dan):
    for i in range(2,10):
        gugu(i)
        print()

dan = input("원하는 단을 입력하세요(예: 2,전체: all)")
if dan == 'all':
    all_gugu(dan)
else:
    gugu(dan)