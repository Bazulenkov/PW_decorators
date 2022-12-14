def decorator_factory(*decorator_args, **decorator_kwargs):
    class Decorator(object):
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print("Inside the decorator with arguments {}".format(decorator_args))
            return self.func(*args, **kwargs)

    return Decorator


@decorator_factory("*****************", "-----------")
def my_simple_func(x):
    return x


print(my_simple_func("Hello"))
