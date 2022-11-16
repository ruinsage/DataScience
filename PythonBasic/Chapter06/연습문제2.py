from statistics import mean
from math import sqrt

x= [5,9,1,7,4,6]
class Scattering:
    #생성자
    def __init__(self,x):
        self.data = x
    #메서드 : 분산 (var_func)
    def var_func(self):
        self.avg = mean(self.data)
        diff = [(d- self.avg) **2 for d in self.data]
        self.var = sum(diff) / (len(self.data) -1)
        print(f"분산: {self.var}")
    #메서드 : 표준편차(std_func)
    def std_func(self):
        std = sqrt(self.var)
        print((f"표준편차: {std}"))

test = Scattering(x)

test.var_func()
test.std_func()
