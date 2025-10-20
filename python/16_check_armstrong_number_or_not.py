num = int(input("enter number : "))

sum = 0
order = len(str(num))
temp = num

while temp > 0:
        digit = temp % 10
        df = digit**order
        sum = sum + df
        temp = temp // 10
    
if sum == num:
     print("this number is armstrong number")
    
else:
     print("this number is not armstrongnumber")
    