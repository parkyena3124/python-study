money=int(input("투입한 돈: "))
price=int(input("물건값: "))
moneyy=money-price
print("거스름돈:",moneyy)
mone=moneyy//500
print("500원 동전의 개수:",mone)
moneyy-=mone*500
moneyy=moneyy//100
print("100원 동전의 개수:",moneyy)