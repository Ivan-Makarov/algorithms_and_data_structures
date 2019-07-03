import random


def getArrayOfInt(SIZE=10, MIN_ITEM=1, MAX_ITEM=100):
    return [random.randrange(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


def bubble_sort(their_array):
    our_array = list(their_array)
    items_to_sort = len(our_array) - 1
    n = 0

    while n < items_to_sort:
        has_swaps = False
        for i in range(items_to_sort - n):
            if our_array[i] < our_array[i + 1]:
                our_array[i], our_array[i + 1] = our_array[i + 1], our_array[i]
                has_swaps = True

        if not has_swaps:
            break

        n += 1

    print(f'It took {n} iterations to sort {len(our_array)} numbers')
    return our_array


array = getArrayOfInt(10, -100, 100)
sorted_array = bubble_sort(array)

print(f'Original list: {array}')
print(f'Sorted list: {sorted_array}')
