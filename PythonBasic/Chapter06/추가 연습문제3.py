class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value += val
        return  self.value

class MaxLimitCalulator(Calculator):

    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value += val
        if self.value >= 100:
            self.value = 100
            return self.value
        else:
            return self.value

cal = MaxLimitCalulator()

cal.add(50)
cal.add(60)

print(cal.value)