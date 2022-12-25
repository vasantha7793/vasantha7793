num=input("enter number value:")
num=input(num)
sum=n
for i in range(2,num+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i, " is prime")
        sum=sum+i
print("sum of prime number is",sum)
