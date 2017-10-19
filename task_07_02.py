import random
from string import digits, ascii_letters, punctuation

def password_generator(n):
    alphabet = list(digits + ascii_letters + punctuation)
    for i in range(n):
        char = random.choice(alphabet)
        yield char

if __name__ == '__main__':
    for i in password_generator(16):
        print(i, sep='', end='')