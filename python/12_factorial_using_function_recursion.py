def fact(a):
    if a == 0:
        return 1 
    else : 
        return(a*fact(a-1))
    
num = int(input("enter number"))
result = fact(num)

print("factorial of given number is",result)
