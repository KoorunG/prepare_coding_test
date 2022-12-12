# 파이썬의 클래스 문법
class CalCulator:
    # 파이썬의 생성자
    # 메모리에 올라오는 순간 즉시 실행
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


cal = CalCulator(1, 2)
cal2 = CalCulator(2, 3)

# print(cal.add())
# print(cal.sub())
# print(cal.mul())
# print(cal.div())

print(cal2.add())

# 클래스 밖에서 바로 수정이 가능함..
cal2.a = 100
print(cal2.add())
