#부모 클래스
class Passbook:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,money): #입금 함수
        self.balance += money
        print(f"입금 금액: {money}")
        print(f"현재 잔액: {self.balance}")
    
    def withdraw(self,money): #출금 함수
        if  self.balance>=money:
            self.balance-=money
            print(f"출금 금액: {money}")
            print(f"현재 잔액: {self.balance}")
        else:
             print("잔액 부족")       
    
    def showInfo(self):
        print(f"예금주: {self.owner}, 현재 잔액: {self.balance}원")

class MinusPassbook(Passbook): #상속
    #withdraw
    def withdraw(self,money):   
       if self.balance-money >= -1000000:
        self.balance-=money
        print(f"출금 금액: {money}")
        print(f"현재 잔액: {self.balance}")
       else:
           print("마이너스 한도 초과")

#실행
#객체 생성 account1 + 생성자 호출(예금주, 잔액)      
account1 = Passbook("홍길동", 100000)
#입금 함수 호출 50,000원 입금
account1.deposit(50000)
#출금하수 호출 (120000)원,(70000)원 출금
account1.withdraw(120000)
account1.withdraw(70000)
account1.showInfo()

#객체 생성 account2 + 생성자 호출(예금주, 잔액)  
account2 = MinusPassbook("김철수", 100000)
#출금하수 호출 (120000)원,(900000)원 출금
account2.withdraw(120000)
account2.withdraw(9000000)
account2.showInfo()