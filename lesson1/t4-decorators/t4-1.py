def decorator(func):
    def wrapper():
        print("I'm decorator")
        return func()

    return wrapper


# @decorator
def my_first_func():
    print("First func")


my_first_func = decorator(my_first_func)

my_first_func()
