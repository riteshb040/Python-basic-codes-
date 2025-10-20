num1 = int(input("enter number : "))
num2 = int(input("enter second number : "))

print("press 1 for addition \npress 2 for substraction \npress 3 for multiplication \npress 4 for division")

choice = int(input("enter number from 1 to 4 : "))

if choice == 1 :
    print(num1 + num2)

elif choice == 2 :
    print(num1 - num2)
    
elif choice == 3 :
    print(num1 * num2)
    
elif choice == 4 :
    print(num1 / num2)
    
else :
    print("invalid inout")