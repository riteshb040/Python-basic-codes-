num = int(input("enter positive number : "))

temp = num
sum = 0

if temp < 0:
    print("please ente positive number")
    
else:
    
    while temp > 0:
        sum = sum + temp
        temp = temp - 1
        
print(sum)
        
        