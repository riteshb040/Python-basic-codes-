# lower = int(input("enter lowest valuse"))
# upper = int(input("enter upper value"))

# for num in range(lower, upper+1):
    
#     if num > 1 :
        
#         for i in range(2,num):
#             if num % i != 0:
#                 print(num,"this number is prime number")
#                 break
#             else:
#                 "this is not prime nummber"
                
                
                
lower = int(input("Enter lowest value: "))
upper = int(input("Enter upper value: "))

for num in range(lower, upper + 1):
    # Prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                # Found a divisor, so number is not prime
                # print(num, "is not a prime number")
                break
        else:
            # This else executes only if the for loop wasn't broken out of
            print(num, "is a prime number")
