import random

print('>>숫자 맞추기 게임<<')
com = random.randint(1,10)

while True:
    my = int(input('예상 숫자를 입력하시오 :'))

    if my == com:
        print("~~ 성공 ~~")
        break
    elif my > com:
        print("더 작은 수 입력")
    elif my < com:
        print("더 큰 수 입력")
    else:
        print("다시 입력하세요")
