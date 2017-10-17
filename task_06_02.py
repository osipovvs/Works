import time

def pause(number_of_seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(number_of_seconds)
            result = func(*args, **kwargs)

            return result
        return wrapper
    return decorator

if __name__ == '__main__':
    @pause(5)
    def func():
        print('The function has been executed with a delay!')

    func()