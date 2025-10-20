num = int(input("enter number "))
fact = 1 

if num < 0 :
    print("factrorial for negative number doses not exist")
    
if num == 0 :
    print("factorial of 0 is  1 ")
    
if num > 1 :
    for i in range(1, num+1):
        fact = fact*i
        
print("factoriual of",num,"is",fact)