import platform

def run_on_linux(func):
    def wrapper(*args, **kwargs):
        os = platform.system()
        return func(*args, **kwargs) if os == 'Linux' else None
    return wrapper


def run_on_windows(func):
    def wrapper(*args, **kwargs):
        os = platform.system()
        return func(*args, **kwargs) if os == 'Windows' else None
    return wrapper

def run_on_macos(func):
    def wrapper(*args, **kwargs):
        os = platform.system()
        return func(*args, **kwargs) if os == 'Darwin' else None
    return wrapper

if __name__ == '__main__':
    @run_on_macos
    def func():
        print("This function can be run only on Windows!")
    
    
    func()
