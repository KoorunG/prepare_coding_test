class Robot:
    # 클래스 변수 선언 - 인스턴스간에 공유가능한 변수
    population = 0

    @classmethod  # 클래스 메소드 선언 - cls는 Class를 의미한다(self와 비슷하게 동작)
    def how_many(cls):
        print(f'We have {Robot.population} robots.')

    def __init__(self, name, code):
        self.name = name                # 인스턴스 변수
        self.code = code
        # 생성자가 호출될 때 마다 클래스 변수 1씩 증가! (인스턴스들이 공유)
        Robot.population += 1

    def robot_say_hi(self):             # 인스턴스 메소드
        print(f'안녕하세요 제 이름은 {self.name} 입니다.')

    def robot_destroyed(self):
        print('{0} is being destroyed'.format(self.name))
        if Robot.population == 0:
            raise IOError('로봇이 존재하지 않습니다.')
        else:
            Robot.population -= 1
            print(f'로봇이 {Robot.population}대 남아있습니다.')

    @staticmethod                       # 파이썬에서의 static method 선언 방법
    def robot_cal_add(a, b):
        return a + b


javis = Robot('javis', 24934534)
siri = Robot('siri', 123675756)

javis.robot_say_hi()
siri.robot_say_hi()

javis.robot_destroyed()
siri.robot_destroyed()

print(Robot.robot_cal_add(2, 3))    # 5

print(Robot.population)             # 2
bixby = Robot('bixby', 45636546)
print(Robot.population)             # 3

Robot.how_many()                    # We have 3 robots.