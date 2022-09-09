x = 0  # глобальная переменная x


def outer():
    x = 50  # x в области видимости объемлющей функции

    def inner():
        x = 100  # локальная переменная x для этой функции
        print(f"inner x is {x}")

    inner()
    print(f"outer x is {x}")


outer()
print(f"global x is {x}")
print("-"*20)


def outer_nonlocal():
    x = 50

    def inner():
        nonlocal x  # нелокальные переменные должны(!) существовать
        x = 100
        print(f"inner x is {x}")

    inner()
    print(f"outer x is {x}")


outer_nonlocal()
print(f"global x is {x}")

# print('globals: ', globals())
