movie_list=["아바타","왕사남","살목지","극한직업"]
print(movie_list)

#메서드(insert, append, remove)
movie_list.insert(1,"범죄도시") #삽입
print(movie_list)

movie_list.append("슈퍼맨") #추가
print(movie_list)

movie_list.remove("살목지") #값을 지정해서 삭제
print(movie_list)

#del : 명령어
del movie_list[2]
print(movie_list) #요소 위치 지정 삭제

x=10
print(x)
del x
#print(x)

print(len(movie_list)) #len : 길이

a=[1,2,3]
print(sum(a))

#90, 50, 80, 70,55 
listt=[90,50,80,70,55]
num=sum(listt)/len(listt)
print(num)