number = int(input("자연수를 입력하세요"))

def is_odd(number):

    if number %2 == 1 :
        print(f"{number}는 홀수입니다")
    else:
        print(f"{number}는 짝수입니다")

is_odd(number)