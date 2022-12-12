def copyright(func):
    def new_func():
        print("@copyright")
        func()
    return new_func


@copyright
def smile():
    print("smile")


def angry():
    print("angry")


def love():
    print("love")


smile = copyright(smile)
angry = copyright(angry)
love = copyright(love)

smile()
angry()
love()
