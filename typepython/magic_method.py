class MagicTest:
    location = "seoul"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '__str__ 오버라이딩'

    def __call__(self):
        return f"{self.name} call!!"

    @classmethod
    def get_location(cls):
        return cls.location


# 파이썬에서는 __init__ 처럼 언더바가 붙은 메소드가 기본으로 제공되는데 이를 매직 메소드라고 한다.
koorung = MagicTest('koorung', 30)

# print(dir(koorung))       # dir() : 해당 인스턴스 객체에 대해 사용가능한 매직 메소드 리스트
print(koorung.__str__())    # '__str__ 오버라이딩'

# 파이썬은 "모든것이 객체" 이다. (클래스, 함수, 타입 모두 포함...)

# () : "실행" 하는 행위
# 보통 인스턴스를 call하면? ( koorung() ) -> TypeError: 'MagicTest' object is not callable
# 클래스에서 __call__을 오버라이딩 하면?

print(koorung())            # koorung call!!  (무려 인스턴스가 callable 해진다)