# Solution 1 (Using Thrid variable)
x = 40
y = 50
temp = x 
print("The temp value is",temp)

x = y
print("The value of the x is", x)

y = temp
print("The value of the y is", y)

# Solution 2 (With out using third variable)
x = 40
y = 50
x , y = y , x
print("The value of x", x)
print("The value of y", y)