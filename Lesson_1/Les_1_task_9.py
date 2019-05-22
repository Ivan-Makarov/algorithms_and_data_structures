# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a > b:
    if a < c:
        print(a)
    elif c > b:
        print(c)
    else:
        print(b)
else:
    if b < c:
        print(b)
    elif c < a:
        print(a)
    else:
        print(c)
