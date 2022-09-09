from functools import wraps


def decorator_factory(input_arg):
    def decorator(func):
        @wraps(func)  # вся магия в этой строке
        def wrapper(*args, **kwargs):
            print(f"arguments of decorator {input_arg}")
            result = func(*args, **kwargs)
            return f"{input_arg}\n{result}\n{input_arg}"

        return wrapper

    return decorator


@decorator_factory("***********************")
def my_simple_func(x):
    return x


print(my_simple_func("Hello"))
print(my_simple_func.__name__)

# arguments of decorator ***********************
# ***********************
# Hello
# ***********************
# my_simple_func
