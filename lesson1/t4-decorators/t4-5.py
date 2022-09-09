from types import MethodType


class Decorator:
    def __init__(self, func) -> None:
        self.func = func
        self.ncalls = 0  # Number of calls of this method

    def __call__(self, *args):
        self.ncalls += 1  # Increment the calls counter
        print("Decorated")
        return self.func(*args)

    def __get__(self, instance, owner):
        return self if instance is None else MethodType(self, instance)


class C:
    @Decorator
    def method(self, x, y):
        print(x + y)


c = C()
c.method(6, 7)
print(c.method.ncalls)

c2 = C()
c2.method(7, 8)
print(c2.method.ncalls)
