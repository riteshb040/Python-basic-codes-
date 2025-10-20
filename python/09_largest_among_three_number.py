a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))

if a1 >= a2 and a1 >= a3:
    print("1st number is the greatest")
elif a2 >= a1 and a2 >= a3:
    print("2nd number is the greatest")
else:
    print("3rd number is the greatest")
