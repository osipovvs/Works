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
    if (b >= c):
        print(a, c, b, sep = ', ')
    elif (c <= a):
        print(c, a, b, sep = ', ')
    else:
        print(a, b, c, sep = ', ')
