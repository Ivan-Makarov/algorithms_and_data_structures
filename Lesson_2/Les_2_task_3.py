# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import math

x = int(input('Input number: '))

reverse = ""


def add_last_digit(x):
  global reverse
  last_digit = x % 10
  reverse = reverse + str(last_digit)


add_last_digit(x)

while x >= 10:
  x = math.floor(x / 10)
  add_last_digit(x)

print('Reversed:', int(reverse))
