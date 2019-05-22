a = float(input("Enter the length of side 1: "))
b = float(input("Enter the length of side 2: "))
c = float(input("Enter the length of side 3: "))

if a < b + c and b < a + c and c < a + b:
    if a == b and b == c and a == c:
        print("Triangle exists and is equilateral")
    elif a == b or b == c or a == c:
        print("Triangle exists and is isosceles")
    else:
        print("Triangle exists")
else:
    print("Triangle does not exist")
