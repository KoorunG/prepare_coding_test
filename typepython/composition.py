# 다른 클래스의 일부 메소드를 사용하고 싶으나, 상속은 사용하고 싶지 않을 경우...
# 파이썬에서 "모든것은 객체" 이다 (원시 자료형이 존재하지 않음)

class Robot:
    """
    Robot Class
    """

    __population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age    # private
        Robot.__population += 1

    @property               # 정보를 숨기기만 하고 읽는것은 가능하게 하고 싶을 경우
    def age(self):          # @property 데코레이터를 사용한다.
        return self.__age   # 자바의 getter과 비슷하다고 보면 된다.

    @age.setter                 # 은닉된 정보의 값을 수정하고 싶을 경우
    def age(self, new_age):     # @변수명.setter 으로 설정하고
        if new_age < 0:
            raise TypeError("age must be over 0")
        self.__age = new_age    # 아래에 함수를 선언하면된다.

    def say_hi(self):
        print(f"Greetings, my masters call me {self.__name}")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.__population} robots."


class BixbyCal:
    def __init__(self, name, age):
        self.Robot = Robot(name, age)

    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b) # 파이썬의 composition