#재귀 호출(함수)(함수 내부에서 자기자신을 호출)
#5!(팩토리얼): 1*2*3*4*5
def fact(n): #fact: 함수명(매개변수는 1개)
    if n==1:
        return 1
    else:
        return n*fact(n-1) #5*fact(4)=120 -> 4*fact(3)=24 -> 3*fact(2)=6 -> 2*fact(1)=2

a=int(input("정수를 입력하세요: ")) #예) 5입력
res=fact(a) #함수 호출, 인수 a(정수) 보냄
#반환되어서 온 결과값을 res 저장
print(a,"!는",res,"이다")

#순환(재귀)함수를 활용하여 1부터 입력받은 숫자까지 합을 구하는 프로그램을 작성
#입력받은 수가 5, 5+4+3+2+1 = 합계
def num(c):
    if c==1:
        return 1
    else:
        return c+num(c-1) #5+num(4)=15 -> 4+num(3)=10 -> 3+num(2)=6 -> 2+num(1)=3

d=int(input("정수를 입력하세요: "))
res2=num(d)
print("1부터",d,"까지의 합계는",res2,"이다")    