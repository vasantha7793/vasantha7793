def ishappy(n):
 sum=0
 while(n!=0):
    r=n%10
    sum=sum+(r*r)
    n=n//10
    return sum
n=int(input())
while(n>9):
    n=ishappy(n)
if n==1 or n==7:
    print('happy number')
else:
    print('no')
