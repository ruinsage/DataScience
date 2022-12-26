import io


class restaurant:
    restaurant_name = None
    cuisine_type = None
    today_visitor = 0
    visitor = 0

    def __init__(self,name,type,visitor,count):
        self.restaurant_name = name
        self.cuisine_type = type
        self.visitor = visitor
        self.today_visitor = 0
        # if self.wite_count == 0:
        #    restaurant.write_file()
        #    self.total_visitor = 0
        # else:
        #    data = restaurant.read_file()
        #    self.total_visitor = data[1]

    def describe_restaurant(self):
        print(f"저희 레스토랑 명칭은 {self.restaurant_name}이고 {self.cuisine_type}전문점입니다")

    def open_restaurant(self):
        print(f"저희 {self.restaurant_name} 레스토랑 오픈했습니다. 어서오세요")

    def visitor_count(self):
        self.today_visitor += self.visitor
        print(f"오늘 총{self.total_visitor}명 방문")

    def write_file(self):
        file = open("data/test.txt",mode='w')
        file.write(f'{restaurant.today_visitor(self)}\t {self.total_visitor}')

    def add_file(self):
        file = open("data/test.txt",mode='a')
        file.write(f'{restaurant.today_visitor(self)}\t {self.total_visitor}')

    def read_file(self):
        file = open("data/test.txt",mode='r')
        lines = file.readline()
        print(lines)
        data = lines(len(lines)).slice()
        print(data)
        return data

    def check(self):
        print(f"오늘 방문자: {self.today_visitor} 누적 방문자: {self.total_visitor}")

    def __del__(self):
        self.day_count += 1

while True:
    #select = input("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분)").split()
    select = ['띵호와','중식']
    name = select[0]
    type2 = select[1]
    count = 0

    test = restaurant(name,type2,0,0)
    test.describe_restaurant()
    test.open_restaurant()
    while True:
        visitor = int(input("방문객 수를 입력하세요.(-1:종료 확인:p)"))
        #visitor = 1
        test2 = restaurant(name,type2,visitor,count)
        if visitor == 'p' and count != 0 :
            test2.read_file()
        elif visitor == -1:
            break
        else:
            test2.visitor_count()
            if count == 0 :
                test2.write_file()
                count += 1
            else:
                test2.add_file()
    if visitor == -1:
        break



