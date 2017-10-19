def fibonacci(n):
    prev = 0
    nxt = 1
    for i in range(n):
        yield nxt
        prev, nxt = nxt, prev + nxt


if __name__ == '__main__':
    for i in fibonacci(10):
        print(i)