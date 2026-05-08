jumin=input("주민번호를 입력하세요: ") #012345-7891011
num=jumin.split("-")[1]
#num=jumin.split("-")
if num[0]=='1' or num[0]=='3':      #num[1][0]
#jumin[7]=='1' or jumin[7]=='3':
    print("남자입니다")
else:
    print("여자입니다")

num2=int(input("숫자1를 입력하세요: "))
num3=int(input("숫자2를 입력하세요: "))
num4=int(input("숫자3를 입력하세요: "))

if num2>=num3 and num2>=num4:
    print("가장 큰 수는",num2)
elif num3>=num2 and num3>=num4:
    print("가장 큰 수는",num3)
else:
    print("가장 큰 수는",num4)

