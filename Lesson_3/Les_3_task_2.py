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
