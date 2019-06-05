import random


def getArrayOfInt(SIZE=10, MIN_ITEM=1, MAX_ITEM=100):
    return [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


array = getArrayOfInt()
print(f'In: {array}')

extreme = {
    'min': {
        'index': 0,
        'value': array[0]
    },
    'max': {
        'index': 0,
        'value': array[0]
    },
}

for i, value in enumerate(array):
    if value < extreme['min']['value']:
        extreme['min']['value'] = value
        extreme['min']['index'] = i

    if value > extreme['max']['value']:
        extreme['max']['value'] = value
        extreme['max']['index'] = i

minI = extreme['min']['index']
maxI = extreme['max']['index']

array[minI], array[maxI] = array[maxI], array[minI]

print(f'Out: {array}')
