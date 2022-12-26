bal = int(input("최초 계좌의 잔액을 입력하세요 :"))
money = int(input("입금액을 입력하세요 :"))
def bank_account (bal):
    balance = bal
    def getBalance () :
        return balance


    def deposit (money) :
        print(f"현재 계좌 잔액은 {balance}")