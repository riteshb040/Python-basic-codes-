nterm = int(input("enter number of terms here"))

result = list(map(lambda x : 2**x , range(nterm+1)))
print(result)


for i in range(nterm + 1):
    print("the value of 2 raised to power",i,"is", result[i])