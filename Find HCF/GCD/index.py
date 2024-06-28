def findHCF(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
        for i in range(1,smaller + 1):
            if ((x%i == 0) and (y%i == 0)):
                HCF = i 
        return HCF
x = 12
y = 30            

print("The HCF of given two numbers is", findHCF(12, 30))
