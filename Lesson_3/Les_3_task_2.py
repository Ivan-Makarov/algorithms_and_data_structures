# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random


def getArrayOfInt(SIZE=10, MIN_ITEM=1, MAX_ITEM=100):
    return [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


array = getArrayOfInt()
result = []

for i, value in enumerate(array):
    if value % 2 == 0:
        result.append(i)

print(array)
print(result)
