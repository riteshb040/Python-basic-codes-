a1 = int(input("enter year :"))

if a1 % 400 == 0  : 
    print("yes leap year")
    
elif a1 % 4 == 0 and a1 % 100 != 0 :
    print("yes leap year")
    
else :
    print("not leap year")    