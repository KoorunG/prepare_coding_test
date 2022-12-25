# 파이썬에서 "모든것은 객체" 이다 (원시 자료형이 존재하지 않음)

class Robot:
    """
    Robot Class
    """

    population = 0

    def __init__(self, name, age):
        self.name = name
        self._age = age         # 파이썬에서 변수명 앞에 __을 붙이면 private 이라는 의미.
                                # 그러나 파이썬 자체가 private을 잘 사용하지 않음
                                # 암묵적으로 _ 만 붙여서 개발자가 접근하지 않도록 가정한다..
        Robot.population += 1

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."


siri = Robot("siri", 30)
print(siri._age)            # 접근은 가능하지만 IDE에서 warning을 보냄