#함수
def add(a, b): #()안에는 매개변수 있어야 함
    return a+b

num=int(input("숫자 입력: "))
num2=int(input("숫자 입력: "))

sums = add(num,num2) #함수 호출(인수), 리턴값을 저장
print(sums)

#sum(): 합계
#len(): 길이
#숫자 리스트의 평균을 반환
def avg(numbers):
    if not numbers:
        return 0
    total=sum(numbers)
    cnt=len(numbers)
    return total/cnt

score_list=[80,90,100,50,70]
aver_res=avg(score_list)
print(aver_res)