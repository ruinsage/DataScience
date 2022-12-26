#age = 10
price = 0
free_tiket = 3
discount_tiket = 5
visitor_count = 0

while True:
    age = int(input("나이를 입력하세요. "))
    visitor_count += 1
    if age >0 and age <=3:
        grade ="유아"
    elif age >3 and age <=13:
        grade = "어린이"
        price = 2000
    elif age >13 and age <=18:
        grade = "청소년"
        price = 3000
    elif age >18 and age <=65:
        grade = "성인"
        price = 5000
    elif age >65:
        grade = "노인"
    else:
        print('다시 입력하세요\n')
        continue

    if price == 0:
        print(f"귀하는 {grade}등급이며 요금은 무료입니다.")
    else:
        if visitor_count %7 == 0 and free_tiket > 0 :
            free_tiket -= 1
            print(f"축하합니다. 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓{free_tiket}장")

        elif visitor_count %4 == 0 and discount_tiket > 0 :
            discount_tiket -= 1
            price = price * 0.7
            print(f"축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓{discount_tiket}장")
        else:
            print(f"귀하는 {grade}등급이며 요금은 {price}원 입니다.")
            pay_type = int(input("요금 유형을 선택하세요.(1: 현금, 2. 공원 전용 신용 카드)"))
            if pay_type == 1:
                cash = int(input("요금을 입력하세요"))
                if cash < price:
                    print(f"{price - cash}가 모자랍니다. 입력하신 {cash}원을 반환합니다")

                elif cash == price:
                    print(f"감사합니다 티켓을 발행합니다")

                else:
                    print(f"감사합니다 티켓을 발행하고 거스름돈 {cash - price}원을 반환합니다")
            elif pay_type == 2:
                price = price * 0.9
                if age >= 60 and age <= 65:
                    print(f'{format(int(price * 0.95), "3,d")}원 결재 되었습니다. 티켓을 발행합니다.')
                else:
                    print(f'{format(int(price), "3,d")}원 결재 되었습니다. 티켓을 발행합니다.')

