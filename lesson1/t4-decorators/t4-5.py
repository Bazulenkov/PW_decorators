def decorator(func):
    def wrapper(*args):
        print("Decorated")
        return func(*args)

    return wrapper


class C:
    @decorator
    def method(self, x, y):
        print(x + y)


c = C()
c.method(6, 7)  # а тут все работает как надо
