# Определить, какое число в массиве встречается чаще всего.

import random


def getArrayOfInt(SIZE=10, MIN_ITEM=1, MAX_ITEM=100):
    return [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]


array = getArrayOfInt(50, 1, 10)
print(f'In: {array}')

frequency = {}

for i in array:
    if frequency.get(i, None) is None:
        frequency[i] = 1
    else:
        frequency[i] += 1

result = {
    'value': None,
    'frequency': None
}

for value, frequency in frequency.items():
    if result['value'] is None:
        result['value'] = value
        result['frequency'] = frequency
    else:
        if frequency > result['frequency']:
            result['value'] = value
            result['frequency'] = frequency

print(f'{result["value"]} is the most frequent number, it occurs {result["frequency"]} times')
