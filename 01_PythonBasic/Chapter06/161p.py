class Account:
    __balace = 0
    __accName = None
    __accNo = None

    def __init__(self,bal,name,no):
        self.__balace = bal
        self.__accName = name
        self.__accNo = no

    def getbalance(self):
        print(f"{self.__accName}님의 계좌에 {self.__balace}원이 조회되었습니다")
        return self.__balace, self.__accName, self.__accNo

    def deposite(self,money):
        if money < 0 :
            print("금액확인")
            return
        self.__balace += money
        print(f"{money}원이 입금되었습니다")

    def withdraw(self,money):
        if money < 0 :
            print("출금확인")
            return
        self.__balace -= money
        print(f"{money}원이 출금되었습니다")

acc = Account(1000,'홍길동','1234-56-7890')
acc.getbalance()

acc.deposite(10000)
acc.getbalance()

acc.withdraw(2000)
acc.getbalance()
