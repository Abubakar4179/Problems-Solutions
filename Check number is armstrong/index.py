num = int(input("Enter the number"))
sum = 0
temp = num
while temp > 0:
    digit = temp%10
    cube = digit**3
    sum = sum + cube
    temp //=10

if sum == num:
    print("It is armstrong number")
else:
    print("It is not armstrong number")


