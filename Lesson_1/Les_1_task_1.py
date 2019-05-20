number = int(input('Enter your 3-digit number:'))

hundreds = number // 100

tens = (number - hundreds * 100) // 10

ones = number - hundreds * 100 - tens * 10

result = hundreds + tens + ones

print('The sum of all digits of your number is', result)
