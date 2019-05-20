x1 = float(input("Enter x coord of point 1: "))
y1 = float(input("Enter y coord of point 1: "))
x2 = float(input("Enter x coord of point 2: "))
y2 = float(input("Enter y coord of point 2: "))

k = (y1 - y2) / (x1 - x2)

if k % 1 == 0:
    k = int(k)

if k == 0:
    k_string = ""
elif k == 1:
    k_string = "x"
else:
    k_string = str(k) + "x"

b = (x1 * y2 - y1 * x2) / (x1 - x2)

if b % 1 == 0:
    b = int(b)

if b > 0:
    b_string = " + " + str(b)
elif b == 0:
    b_string = ""
else:
    b_string = " - " + str(abs(b))

print("Your equation is: y =", k_string + b_string)
