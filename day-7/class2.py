class Board:
    def __init__(self, title, writer): #생성자(객체 생성하면서 초기값을 저장)
        self.title = title
        self.writer = writer
        self.cnt = 0

    def cntup(self):
        self.cnt += 1

board1 = Board("자바의 정성", "홍길동")  #객체 생성 + 생성자 호출
board2 = Board("파이썬 정석", "이순신")

board1.cntup()
board1.cntup()
board2.cntup()

print(board1.title, board1.writer, board1.cnt)
print(board2.title, board2.writer, board2.cnt)
