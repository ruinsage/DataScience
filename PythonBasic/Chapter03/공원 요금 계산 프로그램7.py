age = int(input("나이를 입력하세요."))

if age >= 0 and age <= 3 :
    price = "무료"
    grade = "유아"
elif age > 4 and age <= 13 :
    price = "2000원 "
    grade = "어린이"
elif age > 14 and age <= 18 :
    price = "3000원 "
    grade = "청소년"
elif age > 19 and age <= 65 :
    price = "5000원 "
    grade = "성인"
elif age > 66 :
    price = "무료"
    grade = "노인"
elif age < 0 :
    print("다시 입력하세요")
    quit()

print(f"귀하는 {grade}등급이며 요금은 {price}입니다")
