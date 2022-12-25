i=1
n=int(input())
s=0
while(i<n):
    if n%i==0:
        s=s+i
    i=i+1
if s==n:
    print('perfect number')
else:
    print('not a perfect number')
