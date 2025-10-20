# r1 = int(input("enter range: "))
# d1 = int(input("enter divisable number :"))

# for i in range(r1+1):
#     if i % d1 ==0 :
#         print(i)
    
    
    #using lambda function and filter()
    
l = [39,56,23,78,26,67]

result = list(filter(lambda x : x % 13 == 0 , l ))
print(result)