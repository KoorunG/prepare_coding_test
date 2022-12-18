# 파이썬에서 "모든것은 객체" 이다 (원시 자료형이 존재하지 않음)

class Robot:
    """
    Robot Class
    """

    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."


class Siri(Robot):
    @staticmethod
    def call_me():
        print("네?")

    def cal_mul(self, a, b):
        return a * b


siri = Siri("iphone13 pro")

siri.say_hi()

# mro() : 클래스의 상속관계를 보여주는 메소드
print(Siri.mro())            # [<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]

# 리스트 역시 object가 부모
print(list.mro())            # [<class 'list'>, <class 'object'>]

# 심지어 str, int 역시 object가 부모
print(str.mro(), int.mro())  # [<class 'str'>, <class 'object'>] [<class 'int'>, <class 'object'>]