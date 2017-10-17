from collections import namedtuple

def return_namedtuple(*args, **kwargs):
    def decorator(func):
        def wrapper(*args1, **kwargs1):
            result = func(*args1, **kwargs1)
            names = [*args]

            res_is_tuple = isinstance(result, tuple)
            if res_is_tuple:
                Result = namedtuple('Result', names)
                result = Result(*result)

            return result
        return wrapper
    return decorator

if __name__ == '__main__':

    @return_namedtuple('one', 'two', 'three')
    def func():
        return 1, 2, 3

    @return_namedtuple('first_name', 'last_name', 'age', 'params')
    def func2():
        return 'Kate', 'Winslet', '42', [168, 63]

    print(func())
    print(func2())