fruits = ["사과", "배", "오렌지"] #리스트 0~2

try:
    index = int(input("번호 입력(0~2): "))
    if index <0 or index >= len(fruits):
        raise IndexError #예외를 발생시킴
    #print(fruits[index])
except IndexError:
    print("없는 숫자입니다")
except ValueError:
    print("숫자를 입력하세요")
except Exception as e:
    print("에러메세지", e)
else:
    print(fruits[index])
    #print("정상 작동")
finally:
    print("프로그램 종료")