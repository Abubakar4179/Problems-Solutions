a = "Harry Protter and the Golbet of fire"
w = a.split()
print(w)
for i in range(len(w)):
    w[i] = w[i].lower()

print(w)
w.sort()
print(w)