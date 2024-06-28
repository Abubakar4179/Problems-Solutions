def convertbinary(n):
    if n > 1 :
        convertbinary(n//2)
        print(n%2, end = "")
print("The binary of given number is") 
convertbinary(12)       