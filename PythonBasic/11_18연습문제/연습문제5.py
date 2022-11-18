def gugu(dan):
    for num in range(1,10):
        result = int(dan) * num
        print(result,end='\t')

dan = input("원하는 단을 입력하세요")
gugu(dan)