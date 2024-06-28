num = int(input("Enter the number"))
if num == 1:
    print("It is not prime number")
if num > 1:
    for i in range (2,num):
        if num % 1 ==0 :
            print("It is not prime number")
            break
    else:
        print("It is prime number")            
