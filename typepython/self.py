# self : 인스턴스 객체 그 자체
# (클래스 안의 self의 주소와 인스턴스의 주소는 같음)

class SelfTest:
    # 클래스 변수
    name = "koorung"

    def __init__(self, x):
        self.x = x

    @classmethod
    def func1(cls):
        print(f"cls : {cls}")                          # cls : <class '__main__.SelfTest'>
        print("func1")

    def func2(self):
        print(f"self : {self}")                         # self : <__main__.SelfTest object at 0x104722f70>
        print("클래스 내부의 self 주소 ::: ", id(self))     # 클래스 내부의 self 주소 :::  4369559408


# 1. 인스턴스의 주소
# 2. 클래스의 self의 주소
# 의 값은 같을것이다.
self_test = SelfTest(10)
print(f"인스턴스의 주소 ::: ", id(self_test))              # 인스턴스의 주소 :::  4369559408
self_test.func2()
SelfTest.func1()
print(f"클래스 변수 ::: {self_test.name}")                                  # koorung