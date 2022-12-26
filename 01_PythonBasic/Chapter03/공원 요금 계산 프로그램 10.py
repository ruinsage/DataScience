count_customer = 0 # 파이썬은 스네이크 방식으로
free_tiket = 3
discount_tiket = 5

while True:
    age = int(input("나이를 입력하세요."))
    price = 0

    if age >= 0 and age <= 3 :
        grade = "유아"

    elif age >= 4 and age <= 13 :
        price = 2000
        grade = "어린이"

    elif age >= 14 and age <= 18 :
        price = 3000
        grade = "청소년"

    elif age >= 19 and age <= 65 :
        price = 5000
        grade = "성인"

    elif age >= 66 :
        grade = "노인"

    else:
        print("다시 입력하세요 \n")
        continue

    if price != 0 :
        count_customer += 1

        if free_tiket >0 and count_customer %7 == 0:
            free_tiket = free_tiket - 1
            print(f"축하합니다 1주년 이벤트에 당첨되었습니다. 여기 무료 티켓을 발행합니다. 잔여 무료티켓 {free_tiket}장")

        elif discount_tiket >0 and count_customer %4 == 0:
            discount_tiket -= 1
            print(f"축하합니다. 연간회원권 구매 이벤트에 당첨되셨습니다. 연간 회원 할인 티켓을 발행합니다. 잔여 할인티켓 {discount_tiket}장")

        else:
            print(f"귀하는 {grade}등급이며 요금은 {price}원 입니다")

            cash_card = int(input("요금 유형을 선택하세요. (1: 현금, 2: 공원 전용 신용 카드)"))

            if cash_card == 1:
                charge = int(input("요금을 입력하세요"))

                if  price > charge:
                    print(f"{price - charge}원이 모자랍니다. 입력하신 {charge}원을 반환합니다")

                elif price < charge > 0:
                    print(f"감사합니다. 티켓을 발행하고 거스름돈 {charge-price}원을 반환합니다.")

                else :
                    print(f"감사합니다. 티켓을 발행합니다.")

            elif cash_card == 2:
                price = price * 0.9
                if age >= 60 <= 65:
                    print(f"{int(price * 0.95)}원 결제 되었습니다. 티켓을 발행합니다.")

                elif age >= 4 < 60:
                    print(f"{int(price)}원 결제 되었습니다. 티켓을 발행합니다.")
            else:
                print("현금과 신용카드 중 올바른 선택 값을 입력하십시오")

    elif price == 0 :
        print(f"귀하는 {grade}등급이며 요금은 무료입니다")