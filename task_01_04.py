x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

sqlen_12 = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
sqlen_13 = ((x1 - x3) ** 2 + (y1 - y3) ** 2)
sqlen_23 = ((x3 - x2) ** 2 + (y3 - y2) ** 2)

# s1 = len_12 ** 2
# s2 = len_13 ** 2
# s3 = len_23 ** 2

if (sqlen_12 + sqlen_23 == sqlen_13) or (sqlen_12 + sqlen_13 == sqlen_23) or (sqlen_23 + sqlen_13 == sqlen_12):
    print('Прямоугольный')
else:
    print('Не прямоугольный')

