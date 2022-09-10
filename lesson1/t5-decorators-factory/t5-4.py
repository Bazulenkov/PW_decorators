from functools import wraps


class Decorator(object):
    """Docsting Decorator"""
    def __init__(self, func):
        # Copies name, module, annotations and docstring to the instance.
        self._wrapped = wraps(func)(self)
        # self._wrapped = func

    def __call__(self, *args, **kwargs):
        return self._wrapped(*args, **kwargs)


@Decorator
def test():
    """Docstring of test."""
    pass


print(test.__doc__)
print(test.__name__)

