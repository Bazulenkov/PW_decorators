def decorator_factory(input_arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"arguments of decorator: {input_arg}")
            result = func(*args, **kwargs)
            return f"{input_arg}\n{result}\n{input_arg}"

        return wrapper

    return decorator


@decorator_factory("***********************")
def my_simple_func(x):
    return x


# my_simple_func = decorator_factory("***********************")(my_simple_func)

print(my_simple_func("Hello"))


# @decorator_factory  # Without parentheses
# def test():
#     pass
#
#
# test()
