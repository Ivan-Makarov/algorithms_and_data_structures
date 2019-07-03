import random
from collections import deque


def getArrayOfInt(SIZE=10, MIN_ITEM=1, MAX_ITEM=100):
    return [random.randrange(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def merge(array1, array2):
    result = deque()

    while len(array1) > 0 and len(array2) > 0:
        if array1[0] <= array2[0]:
            result.append(array1[0])
            array1.popleft()
        else:
            result.append(array2[0])
            array2.popleft()

    while len(array1) > 0:
        result.append(array1[0])
        array1.popleft()

    while len(array2) > 0:
        result.append(array2[0])
        array2.popleft()

    return result


def merge_sort(their_array):
    our_array = deque(their_array)

    if len(our_array) <= 1:
        return our_array

    fst_half = deque()
    sec_half = deque()

    for i, value in enumerate(our_array):
        if i < len(our_array) / 2:
            fst_half.append(value)
        else:
            sec_half.append(value)

    fst_half = merge_sort(fst_half)
    sec_half = merge_sort(sec_half)

    return merge(fst_half, sec_half)


array = getArrayOfInt(10, 0, 50)
sorted_array = list(merge_sort(array))

print(f'Original list: {array}')
print(f'Sorted list: {sorted_array}')
