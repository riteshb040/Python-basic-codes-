lower = int(input("enter number "))
upper = int(input("enter number"))


for num in range(lower, upper + 1):
    order = len(str(num))
    
    sum = 0
    temp = num
    while temp > 0 :
        
     digit =  temp % 10
     df = digit**order
     sum = sum + df
     temp = temp // 10
    
    if sum == num:
        print(num)
    