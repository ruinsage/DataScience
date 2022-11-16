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


select_list = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분):").split()
#print(select)
select1 = select_list[0]
select2 = select_list[1]
test = Restaurant(select1,select2)
test.print()