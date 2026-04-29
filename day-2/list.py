#list : 여러값을 순서대로 저장(변경 가능)
list1=[1,2,3,4]
print(list1)
print(list1[2])
list1[3]=500 #값 변경이 가능
print(list1[3])

mix_list=[1,"안녕", 10.3]
print(mix_list) #타입을 혼합하여 가능

#list 안에 list
list2=[100, 200,["안녕",200],300]
print(list2)