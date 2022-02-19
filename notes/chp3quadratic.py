
# finding the roots of a quadratic function ...
import math


a, b, c = eval(input("Enter a, b, c: "))
root_1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
root_2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
print("root1:", root_1, "root 2:", root_2)

# or more cut short and efficiently

a, b, c = eval(input("Enter a, b, c: "))
sqrt_disc = math.sqrt(b ** 2 - 4 * a * c)
den = 2 * a
root_1 = (-b + sqrt_disc) / den
root_2 = (-b - sqrt_disc) / den
print("root1:", root_1, "root 2:", root_2)

