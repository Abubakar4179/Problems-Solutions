print("Mini calculator")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("press 1 for addition\n press 2 for substraction\n press 3 for multiplication\n press 4 for division")
choise = int(input("Enter your choice from 1-4: "))
if choise == 1:
    print(num1 + num2)
elif choise == 2:
    print(num1 - num2)
elif choise == 3:
    print(num1 * num2)
else:
    print(num1 % num2)       

