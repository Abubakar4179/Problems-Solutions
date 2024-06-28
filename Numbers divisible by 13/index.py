# Solution Using for loop
print("The number divisible by 13")
for i in range(1,100):
    if i % 13 == 0:
        print(i)

# Solution using lamda and filter function
l = [39, 48, 26, 33, 98, 67, 87]
result = list(filter(lambda x : x % 13 == 0, l))
print("The number divisible 13 are", result)