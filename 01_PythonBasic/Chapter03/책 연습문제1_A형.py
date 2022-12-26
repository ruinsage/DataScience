weight =int (input("짐의 무게는 얼마입니까?"))
commission = 0

if weight >= 10 :
    commission = 10000
    print(f"수수료는 {format(commission,'3,d')}원 입니다")
else:
    print(f"수수료는 없습니다")

