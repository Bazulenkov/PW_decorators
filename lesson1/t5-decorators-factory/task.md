 Декоратор принимает только один аргумент: функцию, которую нужно украсить. Невозможно передать другие аргументы.

Но часто требуются дополнительные аргументы. Трюк заключается в том, чтобы сделать функцию, которая принимает произвольные аргументы и возвращает декоратор. 

Декораторы могут принимать аргументы. Для этого нужна структура в виде трех уровней вложенности:
1. Верхний уровень сохраняет в себе входные аргументы
2. Средний уровень является собственно самим декоратором
3. Третий уровень необходим для обработки обращений к исходной декорируемой функции
[t5-1.py](course://lesson1/t5-decorators-factory/t5-1.py)
```
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
```

### Важная заметка:

С такими фабриками декораторов вы должны называть декоратор парой круглых скобок:

```python
@decorator_factory # Without parentheses
def test():
    pass

test()

# TypeError: decorator () отсутствует 1 требуемый позиционный аргумент: 'func'
``` 
Для полноты картины, нам с вами осталось обговорить только одну вещь. Раз декоратор заменяет собой
объект функции, то он заменяет и ее имя! Проверим это. Из предыдущего листинга будем использовать
декорированную версию `my_simple_func`.
```
print(my_simple_func.__name__)

# wrapper
```

Получилось, что параметр `__name__` для этой функции не совпадает с ее названием, а является именем
вложенной функции в декоратор. Бывают ситуации, когда это недопустимо. Для решения этого вопроса
призовем стандартную библиотеку Python. Используем из модуля `functools` декоратор `wraps` . И
декорируем им нашу функцию wrapper следующим образом:
[t5-2.py](course://lesson1/t5-decorators-factory/t5-2.py)
```
from functools import wraps


def decorator_with_args(input_arg):
    def decorator(func):
        @wraps(func)  # вся магия в этой строке
        def wrapper(*args, **kwargs):
            print(f"arguments of decorator {input_arg}")
            result = func(*args, **kwargs)
            return f"{input_arg}\n{result}\n{input_arg}"

        return wrapper

    return decorator


@decorator_with_args("***********************")
def my_simple_func(x):
    return x


print(my_simple_func("Hello"))
print(my_simple_func.__name__)

# arguments of decorator ***********************
# ***********************
# Hello
# ***********************
# my_simple_func
```
Как видите, ничего особо сложного нет, если помнить, что в python все есть объект. Успехов!