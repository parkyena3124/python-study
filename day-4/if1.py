# cha=input("영어 한 글자를 입력하세요: ")
# if cha.isupper(): #대문자 -> true 아니면 false
#     print(cha.lower()) #true일때 수행 -> 소문자로 변경
# else:
#     print(cha.upper()) #대문자로 변경

score=int(input("점수를 입력하세요: ")) #81<=score<=100
if 80<score and score<=100: 
    print('A')
elif 60<score and score<=80:
    print('B')
elif 40<score and score<=60:
    print('C')
elif 20<score and score<=40:
    print('D')
else:
    print('E')

