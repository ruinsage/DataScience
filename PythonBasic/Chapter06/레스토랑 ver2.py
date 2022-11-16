class Restaurant:
    name = None
    type = None

    def __init__(self,name,type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"저희 레스토랑 명칭은 '{self.name}'이고 {self.type}전문점입니다")

    def open_restaurant(self):
        print(f"저희 {self.name} 레스토랑이 오픈했습니다")

    def print(self):
        self.describe_restaurant()
        self.open_restaurant()

    def __del__(self):
        print(f"{self.name} 레스토랑 문닫습니다")

select_list = []
for i in range(1,4):
    select = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분):")
    #print(select)
    select = select.split()
    select_list.append(Restaurant(select[0], select[1]))

    #select_list[i].print()
    select_list[i].describe_restaurant()
    select_list[i].open_restaurant()
    print("\n")
print("저녁 10시가 되었습니다")

