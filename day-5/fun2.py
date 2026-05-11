#함수 
#디폴트인수: 함수의 매개변수가 기본값을 갖고 있을 수 있다
def greet(name, msg="별일없지"):
    print("안녕 "+name+" "+msg)

greet("홍길동")

################################
def print_star(n=1): #인수값이 없을 때만 디폴트인수 사용
    print("n=", n)
    for i in range(n):
        print("*******************")

print_star() #인수가 없음
print()
print_star(3) #인수를 3을 보내면서 호출
