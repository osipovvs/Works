import platform

#print(platform.system(), type(platform.system()))

def run_on_linux(func):
    def wrapper(*args, **kwargs):
        os = platform.system()
        result = func(*args, **kwargs)
        if os != 'Linux':
            return None
        return result
    return wrapper


def run_on_windows(func):
    def wrapper(*args, **kwargs):
        os = platform.system()
        result = func(*args, **kwargs)
        if os != 'Windows':
            return None
        return result
    return wrapper

def run_on_macos(func):
    def wrapper(*args, **kwargs):
        os = platform.system()
        result = func(*args, **kwargs)
        if os != 'Darwin':
            return None
        return result
    return wrapper

if __name__ == '__main__':
    @run_on_windows
    def func():
        print("This function can be run only on Windows!")
    
    func()

# os = platform.system()
# if os == 'Windows':
#     print('It is Windows')
# else:
#     print('It is not Windows')
