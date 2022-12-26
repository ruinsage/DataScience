age = int(input("나이를 입력하세요."))
price = ""

if age >= 0 and age <= 3 :
    price = "무료"
elif age > 4 and age <= 13 :
    price = "2000원 "
elif age > 14 and age <= 18 :
    price = "3000원 "
elif age > 19 and age <= 65 :
    price = "5000원 "
elif age > 66 :
    price = "무료"

print(f"요금은 {price}입니다")
