def maker(n):
    y = 8
    def inner(x):
        print('locals: ', locals())
        return x**n, y

    print(inner)
    return inner


in_power_two = maker(2)  # создаем функцию, которая будет возводить что-то в степень
# двойки
in_power_three = maker(3)  # создаем функцию, которая будет возводить что-то в степень
# тройки

print(type(in_power_two))  # убеждаемся, что это точно функция
print(in_power_two(5))  # возводим 5^2 = 25
print(in_power_three(5))  # возводим 5^3 = 125


# def maker(n):
#     return lambda x: x**n
#
#
# in_power_two = maker(2)
# print(in_power_two)
# print(in_power_two(6))
