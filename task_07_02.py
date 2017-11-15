import random
from string import digits, ascii_letters, punctuation

def password_generator(n):
    while True:
        alphabet = list(digits + ascii_letters + punctuation)
        pw = ''.join(random.choice(alphabet) for i in range(n))
        yield pw

if __name__ == '__main__':
    g = password_generator(16)
    print(next(g))