def is_odd(number):
    if number %2 == 0:
        return '짝수'
    else:
        return '홀수'

number = int(input("숫자를 입력하세요"))
print(is_odd(number))

def avg(number_list):
    sum_num = 0
    for num in number_list:
        sum_num += int(num)
    result = sum_num / len(number_list)
    return result

number_list = input('숫자를 입력하세요(예 10 20 30)').split()
print(avg(number_list))

def smile(str):
    print(str,':D')

str = input('문자열을 입력하세요')
smile(str)

def print_max(num1,num2,num3):
    if num1 > num2:
        max_value = num1
    else:
        max_value = num2
    if num2 < num3:
        max_value = num3

    return max_value

number = list(map(int, input('숫자를 입력하세요 (예 10 20 30)').split()))
print(print_max(number[0],number[1],number[2]))

def print_5xn(string):
    for str in range(0,len(string),5):
        print(string[str:str+5])

string = input("문자열을 입력하세요")
print_5xn(string)

def  calc_monthly_salary(annual_salary):
    month_salary  = annual_salary // 12
    return month_salary

annual_salary = int(input("연봉을 입력하세요"))
print(f"월급: {format(calc_monthly_salary(annual_salary),'3,d')}원")

def make_url(message):
    print(f"www.{message}.com")

message = input('중간 url을 입력하세요')
make_url(message)


def input_ingredient(food):
    ingredient_list.append(food)

def make_sandwiches(ingredient_list):
    print()
    print(f'샌드위치를 만들겠습니다')
    for food in ingredient_list:
        print(f"{food} 추가합니다")
    print(f"여기 주문하신 샌드위치를 만들었습니다. 맛있게드세요")


print("안녕하세요 저희 가게에 방문해 주셔서 감사합니다.")
print("1.주문")
print("2.종료")
order = int(input("입력:"))
if order == 1:
    ingredient_list = []
    while True:
        food = input("안녕하세요 원하시는 재료를 입력하세요:")
        if food == '종료':
            break
        else:
            input_ingredient(food)
    make_sandwiches(ingredient_list)