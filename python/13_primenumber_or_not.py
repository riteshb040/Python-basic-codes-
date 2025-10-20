a1 = int(input("enter no. : "))

for i in (2,a1) :
    if a1 % i != 0 :
        print("given number is prime number")
        break
    
    else :
        print("given number is not prime")