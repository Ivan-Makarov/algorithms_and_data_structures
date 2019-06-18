# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import namedtuple

Enterprise = namedtuple('Enterprise', 'name q1 q2 q3 q4 total')

enterprises_count = int(input('Enter enterprises count: '))

enterprises = []
total_income_for_all = 0

for i in range(enterprises_count):
    name = input(f'Enter enterprise {i + 1} name: ')
    q1 = float(input(f'Enter enterprise {i + 1} q1 income: '))
    q2 = float(input(f'Enter enterprise {i + 1} q2 income: '))
    q3 = float(input(f'Enter enterprise {i + 1} q3 income: '))
    q4 = float(input(f'Enter enterprise {i + 1} q4 income: '))
    total = q1 + q2 + q3 + q4
    total_income_for_all += total
    enterprises.append(Enterprise(name, q1, q2, q3, q4, total))

average_income = total_income_for_all / enterprises_count

print(f'Average income: {average_income}')

above_average_income = []
below_average_income = []

for enterprise in enterprises:
    if enterprise.total < average_income:
        below_average_income.append(enterprise.name)
    else:
        above_average_income.append(enterprise.name)

print('Above average:')
print(*above_average_income, sep='\n')
print('Below average:')
print(*below_average_income, sep='\n')
