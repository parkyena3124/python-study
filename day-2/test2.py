ame=int(input("아메리카노 판매 개수: "))
cafe=int(input("카페라떼 판매 개수: "))
capu=int(input("카푸치노 판매 개수: "))
ame*=2000
cafe*=3000
capu*=3500
total= ame+cafe+capu
print("총 매출: "+ str(total)+"원 입니다")
