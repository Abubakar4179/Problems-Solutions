# Solution 1 (Using + operation)
L1 = [1,2,3,4,"e"]
L2 = [7,8,9,"o"]
L12 = L1 + L2
print(L12)

# Solution 2 (Without repitition of values)
L1 = [1,2,3,4,"e","o"]
L2 = [7,8,9,"o"]
L12 = list(set(L1 + L2))
print(L12)