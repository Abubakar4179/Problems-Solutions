year = int(input("Enter the year"))
if (year % 400 == 0) and (year % 100 == 0): 
    print("This is leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("This is leap year")
else:
    print("This is not leap year")    