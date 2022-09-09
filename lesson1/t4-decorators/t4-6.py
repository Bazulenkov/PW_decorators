def decorator_with_args(input_arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"arguments of decorator: {input_arg}")
            result = func(*args, **kwargs)
            return f"{input_arg}\n{result}\n{input_arg}"

        return wrapper

    return decorator


@decorator_with_args("***********************")
def my_simple_func(x):
    return x


print(my_simple_func("Hello"))

# arguments of decorator ***********************
# ***********************
# Hello
# ***********************
