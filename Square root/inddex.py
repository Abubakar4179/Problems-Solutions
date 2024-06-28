# Solution 1 (Using Exponentiation)
num = 64
num1 = int(input("Enter the number"))
sr = num1**(0.5)
print("The square root of the number", sr)

# Solution 2 (Using math module)
import math
num = int(input("Enter the number"))
sr = math.sqrt(num)
print("Square root of the number is", sr)