n = int(input())
p = int(input())
result = []
result2 = []

with open('data.txt') as d:
    raw_data = d.read()
    
    data = raw_data.split(' ')
    for i in data:
        if (int(i) % n) == 0:
            result.append(i)
        result2.append(int(i) ** p)

with open('out-1.txt', 'w') as out1:
    for i in result:
        out1.write("%s " % i)


with open('out-2.txt', 'w') as out2:
    for i in result2:
        out2.write("%s " % i)
