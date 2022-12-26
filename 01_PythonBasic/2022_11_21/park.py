
while True:
    age = int(input("나이를 입력하세요:"))
    grade =""
    price = 0

    if age >0 and age <=3:
        grade = '유아'
    elif age >3 and age <=13:
        grade = '어린이'
        price = 2000
    elif age >14 and age <= 18:
        grade = '청소년'
        price = 3000
    elif age >19 and age <= 65:
        grade = '성인'
        price = 5000
    elif age >65:
        grade= '노인'
    else:
       break

    if price == 0:
        print(f"귀하는 {grade}등급이며 요금은 무료입니다")
    else:
        print(f"귀하는 {grade}등급이며 요금은 {price}원 입니다")
        pay = int(input("요금을 입력하세요:"))
        if pay < price:
            print(f"{price-pay}원이 모자랍니다. 입력하신 {pay}원을 반환합니다")
        elif pay == price:
            print(f"감사합니다. 티켓을 발행합니다.")
        else:
            print(f"감사합니다 티켓을 발행하고 거스름돈 {pay-price}원을 반환합니다")
