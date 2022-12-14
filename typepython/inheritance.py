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


# 파이썬의 상속 -> 그냥 괄호로 부모를 인자로 받으면 된다.
class ChildTestNotModify(MotherTest):
    pass


child_not_modify = ChildTestNotModify('koorung', 30)
print(child_not_modify.location)               # seoul
print(child_not_modify)                        # koorung 오버라이딩
print(child_not_modify())                      # koorung call!!


class ChildTest(MotherTest):
    name = 'child'

    @classmethod
    def call_me(cls):
        print(f"{cls.name} ::: 저요?")

    @staticmethod
    def cal_nul(a, b):
        return a * b


child = ChildTest('koorung2', 50)
child.call_me()                 # cls는 자식 클래스인 ChildTest를 가리킨다.
                                # 즉, cls를 참조할 일이 있으면 @classmethod로 선언하고 아니면 @staticmethod로 선언한다.
print(child.cal_nul(5, 3))