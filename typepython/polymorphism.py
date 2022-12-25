class Robot:
    """
    Robot Class
    """

    __population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age  # private
        Robot.__population += 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("age must be over 0")
        self.__age = new_age

    def say_hi(self):
        print(f"Greetings, my masters call me {self.__name}")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.__population} robots."


class Siri(Robot):
    def say_apple(self):
        print("hello my apple")


class SiriKo(Robot):
    def say_apple(self):
        print("안녕하세요")


class Bixby(Robot):
    def say_samsung(self):
        print("안뇽하세요")


siri = Siri("siri", 10)
siriko = SiriKo("siriko", 15)
bixby = Bixby("bixby", 20)

siri.say_apple()
siriko.say_apple()