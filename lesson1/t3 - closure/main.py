def some_func():
    return "I am function"


def maker(n):
    y = 8

    def inner(x):
        return x**n

    print(inner)
    return inner


def in_power_two(x):
    n = 2
    return x**n


in_power_two = maker(2)  # создаем функцию, которая будет возводить что-то в степень
# двойки
in_power_three = maker(3)  # создаем функцию, которая будет возводить что-то в степень
# тройки
pass


print(type(in_power_two))  # убеждаемся, что это точно функция
print(in_power_two(5))  # возводим 5^2 = 25
print(in_power_three(5))  # возводим 5^3 = 125

# elems = in_power_two.__closure__
# values = [value.cell_contents for value in elems]
# print("Closure values: ", values)


def maker(n):
    return lambda x: x**n
