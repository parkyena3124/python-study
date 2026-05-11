#숫자 입력 -> 출력 반복, 0을 입력하면 종료

while(1):
    num=int(input("숫자 입력: "))
    print(num)
    if num==0:
        break

a=True
while a: #True(참) 반복, False(거짓) 탈출
    sum=int(input("입력: "))
    print(sum)
    if num==0:
        a=False

print("반복문 종료")

print("="*20)

menu=["쫄면", "김밥","냉면","오뎅"]
b=input("메뉴 선택: ")
while b in menu: #조건이 참일때 수행 #in은 포함 연산자
    print(b)
    b=input("메뉴 선택: ")
    #while 문장 안에서 반드시 거짓으로 변경되는 문장이 나와야함