#문자열
s="Hello python"
print(s[6]) #인덱싱
print(s[6:12]) #슬라이싱

jumin="080420-4321456"
print("성별: "+ jumin[7]) #-7
print("월: "+ jumin[2:4]) #2~3, -12:10
print("일: "+ jumin[4:6]) #4~5, -10:-8
print("뒷자리: "+ jumin[7:]) #7~끝

s1="나는 학생입니다"
s2="파이썬을 배웁니다"
s3='재미있습니다'
s4="""  #여러 문자열을 저장할때, 입력한 그대로 저장
나는 학생입니다
파이썬을 배웁니다
재미있습니다
"""
print(s4)

year="1978"
month="03"
day="20"
date=year+"-"+ month +"-"+day
print(date)

date2=date.split('-')
print(date2)
print(type(date2))
print(date[5:7])
print(date2[1][0:2], end="*")

name="kakao taxi"
name2=name.replace("k","t",1)
print()
print(name2)

print("python"*5) #반복

#문자열에서 ,(컴마)제거
won="63,120,450"
won2=won.replace(","," ",2)
print(won2)

won3=345908800
won4=format(won3, ",d")
print(won4)

#문자열 대소문자, 길이
p="Python is Amazing"
print(p.lower()) #소문자
print(p.upper()) #대문자
print(p.capitalize()) #첫글자 대문자
print(p[0].isupper()) #Ture
print(len(p)) #길이
print(p.count("i")) #개수

#위치
index=p.index("i") #7
print(index)
index=p.index("i", index+1) #14
print(index)

#문자열 연결
words = ["Python", "is", "easy"]
result= " ".join(words) #" " -> 사이에 공백 넣으면서 연결
print(result)

#제거
text="  Hello   Python****"
print(text.strip()) #공백 제거
print(text.rstrip('*')) #오른쪽 * 제거, .lstrip():왼쪽부터

#자리수만큼 0으로 채우기
num="5"
result=num.zfill(3)
print(result)

#format
age=19
print("나는 %d살입니다" %age) #19를 %d 자리에 넣음
print("나는 {}살입니다".format(age))

like="노래부르기"
print("나는 %d살이고 %s를 좋아해요" %(age, like))
print("나는 {0}살이고 {1}를 좋아해요".format(age,like))
#f 스트링
print(f"나는 {age}살이고 {like}를 좋아해요")

print("나의 주소는 {addr}이며, 나의 키는 {height}cm 입니다".format(addr="인천",height=165))

#이스케이프(탈출) 문자
print("\n배우는 과목은\n \"파이썬\" 입니다") 
#\r: 커서를 맨 앞으로 이동
print("red apple\rpine") #\r은 맨 앞으로
print("i like you!\b!!") #\b는 한 글자 삭제
print("red\t apple") #\t는 탭 이동

#인덱스 찾기
p="Python is Amazing"
print(p.find("A")) #왼쪽부터 찾아서 인덱스 번호 출력, 10
print(p.rfind("A")) #오른쪽부터
print(p.index("a")) #왼쪽부터 찾아서 인덱스 번호 출력, 12
print(p.rindex("a")) #오른쪽부터

print(p.find("java")) #없는 문자를 찾으면 -1
#print(p.index("java")) #없는 문자를 찾으면 에러발생

arr_Str=input('Input String : ').split('-') #information-technology -> -(하이퍼) 기준으로 쪼갬 [0][1] 나누어서
arr_Len=int(input('Input Number : ')) #12 
arr_Val=list(range(0, arr_Len,2)) #0 2 4 6 8 10
arr_Val.remove(4) #4라는 값 삭제 -> 0 2 6 8 10
print(arr_Str[1].find('i')+arr_Val[2])
#technology에서 i 찾음 find할때 없으면 -1
#-1 + arr_Val[2] -> 6 =5
