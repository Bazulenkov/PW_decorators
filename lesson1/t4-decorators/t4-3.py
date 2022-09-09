class Decorator:
    def __init__(self, func) -> None:
        self.func = func

    def __call__(self, *args):
        self.func(*args)
        print("Decorated")


class C:
    @Decorator
    def method(self, x, y):
        print(x + y)


c = C()
c.method(1, 2)  # нам нужен в явном виде self, а его нет и случается ошибка
