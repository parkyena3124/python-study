name=input("이름: ")
price=int(input("가격: "))
num=int(input("수량: "))
print(name,"의 총 금액은",(num*price),"원입니다.")
print(name+"의 총 금액은 "+str(num*price)+"원입니다.")
print(f"{name}의 총 금액은 {num*price}원입니다.")
#print 안에서 f는 f-string이라하며 포맷 문자열
# ==> f"{변수 값}"
#숫자 -> 문자로 변환 : str
#실수는 float만 있음(8바이트)