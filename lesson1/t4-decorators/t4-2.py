class Tracer:
    def __init__(self, func) -> None:
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Calls {self.calls} to {self.func.__name__}")
        return self.func(*args, **kwargs)


# @Tracer
def spam(a, b, c):
    return a + b + c



print(spam)
spam = Tracer(spam)

print(spam(1, 2, 3))
print(spam("a", "b", "c"))
print(spam)

