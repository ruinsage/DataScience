
ingredient_list = []
def input_ingredient():

    while True:
        select2 = input("안녕하세요. 원하시는 재료를 입력하세요 :")
        if select2 == "종료" :
            print()
            return ingredient_list

        else:
            ingredient_list.append(select2)

def make_sandwiches(ingredient_list) :
    print(f"샌드위치를 만들겠습니다")
    for food in ingredient_list :
        print(f"{food} 추가합니다")
    print(f"\n여기 주문하신 샌드위치 만들었습니다. 맛있게 드세요.\n")


while True:
    print(f"안녕하세요. 저희 가게에 방문해 주셔서 감사합니다")
    print("1.주문")
    print("2.종료")

    select = int(input("입력:"))

    if select == 2:
        break

    input_ingredient()

    make_sandwiches(ingredient_list)