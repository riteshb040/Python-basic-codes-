def findHCF(x,y):
 if x > y:
    smaller = y
 else:
     smaller = x
     
 for i in range(1, smaller + 1):
     if (x % i == 0) and (y % i == 0):
        HCF = i
        
 return HCF

print("the HCF of given two number is", findHCF(12,30))
    
    
