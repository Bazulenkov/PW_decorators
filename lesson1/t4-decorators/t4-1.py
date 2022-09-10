def decorator(func):
    def wrapper():
        print("I'm decorator")
        result = func()
        result += " added decorator"
        return result

    return wrapper



# @decorator
def my_first_func():
    print("Original function")
    return "First func"

print(my_first_func)

a = 0
a = a + 1

my_first_func = decorator(my_first_func)
print(my_first_func)


a = my_first_func()
print(a)
pass