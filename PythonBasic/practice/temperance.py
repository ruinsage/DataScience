
temperance = {'월':25.5,'화':28.3,'수':33.2,'목':32.1,'금':17.3,'토':35.3,'일':33.3}
class temperance_class():
    def __init__(self,temperance):
        self.temperance = temperance
    def display(self):
        print('-' * 53)
        for temp in self.temperance:
            print(f" {temp}\t\t", end='')
        print()
        print('-' * 53)
        for i in self.temperance.values():
            print(f"{i}\t", end='')
        print()
        print('-' * 53)

    def min_temp(self):
        min_temp = 100
        for value in self.temperance.values():
            if min_temp > value:
                min_temp = value
        print(f'가장 낮은 최고 기온 : {min_temp}')

    def over_temp(self,num):
        day_temp30 = []
        for day in self.temperance:
            if self.temperance[day] >= num:
                day_temp30.append(day)
        day_temp30 = ', '.join(day_temp30)
        print(f'기온이 {num}℃ 이상인 요일: {day_temp30}')

    def avg_temp(self):
        sum_temp = 0
        for temp in self.temperance.values():
            sum_temp += int(temp)
        print(f'일주일간의 최고 기온의 평균 : {sum_temp / 7}')

while True:
    print("기능을 선택하세요(예 1)")
    menu = int(input('1-주간기온 2-주간 최저기온 3-입력한 온도 이상인 요일 4-주간 평균 기온 그외키-종료:'))
    temperance_week = temperance_class(temperance)
    if menu == 1:
        temperance_week.display()
    elif menu == 2:
        temperance_week.min_temp()
    elif menu == 3:
        target_temp = int(input("기준온도를 입력하세요"))
        temperance_week.over_temp(target_temp)
    elif menu == 4:
        temperance_week.avg_temp()
    else:
        break


