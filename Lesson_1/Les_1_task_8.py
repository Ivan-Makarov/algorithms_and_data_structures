year = int(input("Enter year: "))

common = str(year) + ' is a common year'
leap = str(year) + ' is a leap year'

if year % 400 != 0:
    if year % 100 != 0:
        if year % 4 != 0:
            print(common)
        else:
            print(leap)
    else:
        print(common)
else:
    print(leap)
