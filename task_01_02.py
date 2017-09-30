plates = int(input())
w_liquid = float(input())

while (plates > 0) and (w_liquid > 0):
    w_liquid -= 0.5
    plates -= 1

if w_liquid > 0:
    print('All the plates have been washed', w_liquid, 'liters left')
elif plates > 0:
    print('Liquid is over,', plates, 'plates are left')
else:
    print('All the plates are washed, and there is no more liquid')