
#부모클래스
class Employee:
    name = None
    pay = 0

    def __init__(self,name):
        self.name = name

class Permanent (Employee):

    def __init__(self,bpay,bonus):
        Employee().__init__(name)
        self.pay = bpay + bonus
class Temporary (Employee):

    def __init__(self,time,tpay):
        Employee().__init__(name)
        self.tpay = tpay * time

empType = input("고용형태 선택(정규식 <P>, 임시직<T>) : >? ")

if empType == 'P' or empType == 'p':
    name = input("이름: >?")
    pay = int(input("기본급 : >?"))
    bonus = int(input("상여금 : >?"))
    permanent = Permanent(name,pay,bonus)


elif empType == 'T' or empType == 't':
    name2 = input("이름: >?")
    time = int(input("작업시간: >?"))
    tpay = int(input("시급: >?"))
    temporary = Temporary(name2,time,tpay)
    print('=' *30)

else:
    print('='*30)
    print('입력오류')
