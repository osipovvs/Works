def bubble_sort(lst):
    for i in range(1, len(lst)):    # Внешний цикл, идёт, пока в списке есть неотсортированные пары эл-тов
        flag = 0 # Метка, равенство нулю которой после выполнения внутреннего цикла свидетельствует о том, что список отсортирован
        for j in range(len(lst) - i): # dвнутренний цикл, в к-ром реализуется попарное сравнение элементов списка
            if lst[j] > lst[j+1]: # если рассматриваемый эл-т больше своего соседа справа, 
                lst[j], lst[j+1] = lst[j+1], lst[j] # то мы меняем их местами
                flag += 1 # и ставим метку того, что нам пришлось что-то менять, список не был отсортирован
        if flag == 0: # переставляя эл-ты, мы постепенно "улучшаем" наш список, в конце концов наступает итерация, на которой нам не нужно никого менять местами
            break # Цикл сделал своё дело, цикл может уходить! Ну, или мы -- из цикла.
    return lst
