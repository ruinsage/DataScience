
class FourCal:
    first = second = 0


    def __init__(self,first,second):
        if first != 0 and second != 0:
            self.first = first
            self.second = second
        else :
            self.setdata(first,second)

    def setdata(self,first,second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        print(result)

    def mul(self):
        result = self.first * self.second
        print(result)

    def sub(self):
        result = self.first - self.second
        print(result)

    def div(self):
        result = self.first / self.second
        print(result)

a = FourCal(0,0)
b = FourCal(3,8)
a.setdata(4,2)
a.add()
a.mul()
a.sub()
a.div()

b.add()
b.mul()
b.sub()
b.div()

