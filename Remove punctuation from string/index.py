punc = '''@!#$%^&^&<>()*...'''
Stringe = input("Enter the word\n")
empty_str = ""
for i in Stringe:
    if i not in punc:
        empty_str += i

print(empty_str)