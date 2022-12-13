class Robot:
    """
    [Doc test]
    __doc__ 으로 접근한다.
    """

    # 클래스 변수 선언 - 인스턴스간에 공유가능한 변수
    population = 0

    @classmethod  # 클래스 메소드 선언 - cls는 Class를 의미한다(self와 비슷하게 동작)
    def how_many(cls):
        print(f'We have {Robot.population} robots.')

    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code
        # 생성자가 호출될 때 마다 클래스 변수 1씩 증가! (인스턴스들이 공유)
        Robot.population += 1

    def robot_say_hi(self):  # 인스턴스 메소드
        print(f'안녕하세요 제 이름은 {self.name} 입니다.')

    def robot_destroyed(self):
        print('{0} is being destroyed'.format(self.name))
        if Robot.population == 0:
            raise IOError('로봇이 존재하지 않습니다.')
        else:
            Robot.population -= 1
            print(f'로봇이 {Robot.population}대 남아있습니다.')

    @staticmethod  # 파이썬에서의 static method 선언 방법
    def robot_cal_add(a, b):
        return a + b


javis = Robot('javis', 24934534)
siri = Robot('siri', 123675756)


# 파이썬은 메모리 효율을 위해 인스턴스 메소드도 인스턴스 네임스페이스가 아닌 클래스의 네임스페이스에 정보를 저장한다.

# __dict__ : 파이썬의 네임스페이스에 접근
print(Robot.__dict__)  # {'__module__': '__main__', 'population': 2, 'how_many': <classmethod object at 0x100804fd0>,
# '__init__': <function Robot.__init__ at 0x100801e50>, 'robot_say_hi': <function Robot.robot_say_hi at 0x100802550>,
# 'robot_destroyed': <function Robot.robot_destroyed at 0x1008025e0>, 'robot_cal_add': <staticmethod object at
# 0x100804fa0>, '__dict__': <attribute '__dict__' of 'Robot' objects>, '__weakref__': <attribute '__weakref__' of
# 'Robot' objects>, '__doc__': None}

# 때문에 인스턴스.__dict__ 로는 인스턴스 메소드의 정보가 나오지 않는다.
print(siri.__dict__)  # {'name': 'siri', 'code': 123675756}
print(javis.__dict__)  # {'name': 'javis', 'code': 24934534}

# 그러나 인스턴스에서 인스턴스 메소드를 호출하면 처음으로 인스턴스 네임스페이스에 접근하고, 그곳에 없으면 클래스 네임스페이스에 접근해서 메소드를 호출한다.

# 즉, 인스턴스에서 클래스 변수나 클래스 메소드에 접근할 수 있다는 것을 이 원리로 설명할 수 있다. (파이썬에서 이런 방식으로 메모리 최적화를 한 것임)
print(siri.population)
print(javis.how_many())

# 단, 클래스에서 인스턴스 메소드를 호출하는 것은 불가능한데
try:
    Robot.robot_say_hi()
except:
    print('클래스에서 인스턴스 메소드를 호출하는 것은 불가능')

# 인자에 인스턴스를 집어넣으면 인스턴스에서 메소드에 접근하는 것과 완전히 동일한 코드가 된다.
Robot.robot_say_hi(siri)
siri.robot_say_hi()

# dir() : 인스턴스를 통해서 "접근할 수 있는 호출"을 보여줌
print(dir(siri))  # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', '__weakref__', 'code', 'how_many', 'name', 'population', 'robot_cal_add', 'robot_destroyed',
# 'robot_say_hi']

# __doc__ : 인스턴스의 주석에 접근
print(siri.__doc__)


# __class__ : 인스턴스가 어떤 클래스인지 확인
print(siri.__class__)
print(javis.__class__)
print(Robot.__class__)