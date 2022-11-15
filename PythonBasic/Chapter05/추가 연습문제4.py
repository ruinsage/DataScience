numbers = input("세개의 숫자를 입력하세요 예) 10 20 30")
#numbers = "10 20 30"
#print(numbers)
number_list = numbers.split()
#print(number2)

def print_max(number_list):
    max_num = 0
    for number in number_list:
        if int(number) > int(max_num):
            #print(number)
            #print(befor_num)
            max_num = number
    print(f"가장 큰 수 : {max_num}")

print_max(number_list)
