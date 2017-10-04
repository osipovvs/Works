a = int(input())
b = int(input())
c = int(input())

if (a >= b):
    if (b >= c):
         print(c, b, a, sep = ', ')
    elif (c >= a):
        print(b, a, c, sep = ', ')
    else:
        print(b, c, a, sep = ', ')
else:
    if (c <= a):
        print(c, a, b, sep = ', ')
    elif (b <= c):
        print(a, b, c, sep = ', ')
    else:
        print(a, c, b, sep = ', ')
