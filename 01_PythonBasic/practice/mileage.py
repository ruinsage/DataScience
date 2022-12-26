class mileage_class:
    def __init__(self, mileage_data):
        self.mileage_dict = mileage_data
    def display(self):
        for client in self.mileage_dict:
            print(f"아이디: {client}, 마일리지: {self.mileage_dict[client]}점")
    def update(self,id,value):
        self.mileage_dict[id] = value
        print(f"{id}님의 마일리지({value}점)가 수정되었습니다")
    def add(self,id,value):
        self.mileage_dict[id] = value
        print(f"{id}님의 마일리지({value}점)가 추가되었습니다")
    def max(self):
        max_value = 0
        print(self.mileage_dict)
        for item in self.mileage_dict.items():
            if max_value < int(item[1]):
                max_value = item[1]
                target_id = item[0]
            else:
                pass
        print(f"{target_id}님의 {self.mileage_dict[target_id]}점이 가장 높은 점수입니다")
    def __del__(self):
        print()

mileage_data = {'kim99': 12000, 'lee66': 11000, 'han55': 3000, 'hong55': 5000, 'hwang33': 18000}
while True:
    mileage = mileage_class(mileage_data)
    command = int(input("사용하실 마일리지 메뉴를 선택하세요(1:고객정보 확인 2:마일리지 수정 3:고객정보 추가 4:마일리지 최대값확인 -1: 종료)"))
    if command ==1:
        mileage.display()
    elif command ==2:
        id,value = input('수정할 고객 아이디와 마일리지를 입력하세요. (예: han55 5000)').split()
        mileage.update(id,value)
    elif command == 3:
        id,value = input('추가할 고객 아이디와 마일리지를 입력하세요. (예: han55 5000)').split()
        mileage.add(id,value)
    elif command == 4:
        mileage.max()
    elif command == -1:
        break
    else:
        break