x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())

len_12 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
len_13 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
len_23 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5

s1 = len_12 ** 2
s2 = len_13 ** 2
s3 = len_23 ** 2

if (s1 + s2 == s3) or (s1 + s3 == s2) or (s2 + s3 == s1):
    print('Square')
else:
    print('Nonsquare')



# len_hyp = 0

# sides = (len_12, len_13, len_23)

# for i in (len_12, len_13, len_23):
#     if i > len_hyp:
#         len_hyp = i

# if 

