# Solution 1 (Using for loop)
num = int(input("Enter the number"))
fact = 1
if num < 0:
    print("Does not exist")
if num == 0:
    print("The factorial of zero is", 1) 
if num > 0:
    for i in range(1 , num+1):
        fact = fact*i
print("Factorial is", fact)    

# Solution 2 (Using Recursion)
def fact(a):
    if a == 0:
        return 1
    else:
        return (a) * (fact(a-1))
num = int(input("Enter the number"))
Result = fact(num)
print("Factorial of number is", Result)    
       