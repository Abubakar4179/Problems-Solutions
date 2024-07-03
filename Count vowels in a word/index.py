# Solution 1 (Using Dictionary)
a = "Harry Portter and the prisoner of Azkaban"
vowels= "aeiou"
a = a.casefold()
count = {}.fromkeys(vowels, 0)
for char in a:
    if char in count:
        count[char] += 1

print(count)

# Solution 2(Using list and dictionary comprihension)
a = "Harry Portter and the prisoner of Azkaban"
vowels= "aeiou"
a = a.casefold()
count = {key:sum([1 for char in a if char == key]) for key in vowels}
print(count)