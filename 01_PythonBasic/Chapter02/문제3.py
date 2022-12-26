fat = 25
carbohydrate = 520
protein = 45
sum = (fat * 9) + (protein * 4) + (carbohydrate * 4)
print(f"지방의 그램을 입력하세요 : {fat}")
print(f"탄수화물의 그램을 입력하세요 : {carbohydrate}")
print(f"단백질의 그램을 입력하세요 : {protein}")
print(f"총칼로리 : {format(sum,0,3)} cal")