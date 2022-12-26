weight =int (input("짐의 무게는 얼마입니까?"))
weightcounter = 0
commission = 0

if weight >= 10:
    weightcounter = int(weight / 10)
if weight >= 10 :
    commission = weightcounter
    print(f"수수료는 {commission}0,000 원 입니다")
else:
    print(f"수수료는 없습니다")

