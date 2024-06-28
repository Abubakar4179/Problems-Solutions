def fact(n):
    if n == 1 :
        return 1
    else:
        return (n * fact(n-1))
    
n = int(input("Enter the number"))
if n <=0:
    print("Factorial of less than 1 cant existed") 
else:
    print("Factorial of number is", fact(n))       