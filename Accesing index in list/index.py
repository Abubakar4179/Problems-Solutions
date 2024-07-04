# Using Enumerate method
list = [90,91,92,98]
for index, value in enumerate(list):
    print(index,"-", value)

# Not Using Enumerate method  

list = [90,91,92,98]
for index in range(len(list)):
    value = list[index]
    print(index,"-",value)