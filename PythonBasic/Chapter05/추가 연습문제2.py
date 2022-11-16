number = input("평균을 낼 숫자들을 입력하세요 예) 10, 20, 30, 6")
#number = "10,20,30"
number_list = number.split(',')
#print(number_list)

#number_list = number.split(',')
#print(number2)
#print(len(number2))

def number_avg (number_list) :
    sum = 0
    for num in number_list:
        #print(num)
        sum += int(num)
    #print(f"sum : {sum}")
    avg = sum / len(number_list)
    print(f"입력하신 숫자들의 평균 :", format(avg,"1.1f"))

number_avg(number_list)

