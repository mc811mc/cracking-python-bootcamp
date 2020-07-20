import math

#addition
a1 = float(input("Addition - Enter first number: "))
a2 = float(input("Enter second number: "))
addition = a1 + a2
print(a1, "+", a2, "=", addition)

#subtraction
a1 = float(input("Subtraction - Enter first number: "))
a2 = float(input("Enter second number: "))
subtraction = a1 - a2
print(a1, "-", a2, "=", subtraction)

#multiplication
a1 = float(input("Multiplication - Enter first number: "))
a2 = float(input("Enter second number: "))
multiplcation = a1 * a2
print(a1, "x", a2, "=", multiplcation)

#division
a1 = float(input("Division - Enter first number: "))
a2 = float(input("Enter second number: "))
division = a1 / a2
print(a1, "/", a2, "=", division)

#modulus
a1 = float(input("Modulus - Enter first number: "))
a2 = float(input("Enter second number: "))
modulus = a1 % a2
print(a1, "%", a2, "=", modulus)

#square_root
a1 = float(input("Square Root - Enter first number: "))
sqrt = math.sqrt(a1)
print("√", a1, "=", sqrt)

#exponentiation
a1 = float(input("Exponentiation - Enter base number: "))
a2 = float(input("Enter power: "))
exp = math.pow(a1, a2)
print(a1, "raised to the power of ", a2, "is", exp)

#sin
a1 = float(input("Sin - Enter angle: "))
sin = math.sin(a1)
sin_d = math.sin(math.radians(a1))
print("Sin(", a1,") =", sin, "r")
print("Sin(", a1, ") =", sin_d, "°")

#cos
a1 = float(input("Cos - Enter angle: "))
cos = math.cos(a1)
cos_d = math.cos(math.radians(a1))
print("Cos(", a1, ") =", cos, "r")
print("Cos(", a1, ") =", cos_d, "°")

#tan
a1 = float(input("Tan - Enter angle: "))
tan = math.tan(a1)
tan_d = math.tan(math.radians(a1))
print("Tan(", a1, ") =", tan, "r")
print("Tan(", a1, ") =", tan_d, "°")

#logarithm
a1 = float(input("Logarithm - Enter number: "))
a2 = float(input("Enter base: "))
exp = math.log(a1, a2)
print("Log", a1, "base", a2, "=", exp)
