class calc_class :
    x = y = 0

    def __init__(self,a,b):
        self.x = a
        self.y = b

    def plus(self):
        p = self.x + self.y
        return p
    def minus(self):
        m = self.x - self.y
        return m

obj = calc_class(20,50)
print(obj.plus())
print(obj.minus())



