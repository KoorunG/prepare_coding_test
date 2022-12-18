class MotherTest:
    location = "seoul"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} 오버라이딩'

    def __call__(self):
        return f"{self.name} call!!"

    @classmethod
    def get_location(cls):
        return cls.location

    def say_hi(self):
        print(f'hello {self.name}')


# 파이썬의 상속 -> 그냥 괄호로 부모를 인자로 받으면 된다.
class ChildTestNotModify(MotherTest):
    pass


child_not_modify = ChildTestNotModify('koorung', 30)
print(child_not_modify.location)               # seoul
print(child_not_modify)                        # koorung 오버라이딩
print(child_not_modify())                      # koorung call!!


class ChildTest(MotherTest):
    name = 'child'

    # 부모클래스인 MotherTest의 호출을 그대로 불러올 수 있다. (IDE단에서 지원)
    def __init__(self, name, age):
        super().__init__(name, age)

    @classmethod
    def call_me(cls):
        print(f"{cls.name} ::: 저요?")

    @staticmethod
    def cal_nul(a, b):
        return a * b

    @classmethod
    def get_location(cls):
        print(f'부모 호출 ::: {super().get_location()} 자식 호출 ::: {cls.location}')

    def say_hi(self):
        print(f'say_hi {self.name}')


mother = MotherTest('mother', 30)
mother.say_hi()                 # hello motherÍ

child = ChildTest('child', 10)
child.say_hi()                  # say_hi child
child.get_location()