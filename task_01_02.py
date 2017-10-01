plates = int(input())
w_liquid = float(input())

while (plates > 0) and (w_liquid > 0):
    w_liquid -= 0.5
    plates -= 1

if w_liquid > 0:
    print('Все тарелки вымыты. Осталось ', w_liquid, 'ед. моющего средства')
elif plates > 0:
    print('Моющее средство закончилось. Осталось ', plates, 'тарелок')
else:
    print('Все тарелки вымыты, моющее средство закончилось')