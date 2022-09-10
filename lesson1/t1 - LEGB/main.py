x = 0  # глобальная переменная x


def outer():
    x = 50  # x в области видимости объемлющей функции
    y = 2

    def inner():
        x = 100  # локальная переменная x для этой функции
        print(f"inner x is {x}")
    inner()
    print(f"outer x is {x}")


outer()
print(f"global x is {x}")
print("-"*20)
pass
