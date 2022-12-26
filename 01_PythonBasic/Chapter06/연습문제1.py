print("사각형의 넓이와 둘레를 계산합니다")
w = int(input("사각형의 넓이: "))
h = int(input("사각형의 둘레: "))

class Rectangle:
    width = 0
    height = 0

    def __init__(self,w,h):
        self.width = w
        self.height = h

    def area_calc(self):
        area = self.width * self.height
        return area

    def circum_calc(self):
        circum = (self.width + self.height) * 2
        return circum

#w = 10
#h = 5
result = Rectangle(w,h)
print("-"*30)
area = result.area_calc()
print(f"사각형의 넓이 : {area}")
circum = result.circum_calc()
print(f"사각형의 둘레 : {circum}")
print("-"*30)