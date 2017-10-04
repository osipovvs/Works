def average(lst):
    sum = 0
    avg = 0
    for i in lst:
        sum += i
    avg = (sum / len(lst))

    return(round(avg, 3))
