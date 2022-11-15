numbers = input("세개의 숫자를 입력하세요")
#numbers = input("세개의 숫자를 입력하세요")
#print(numbers)
number2 = numbers.split()
#print(number2)

def print_max(number2):
    max_num = 0
    for number in number2:
        if int(number) > int(max_num):
            #print(number)
            #print(befor_num)
            max_num = number
    print(f"가장 큰 수 : {max_num}")

print_max(number2)
