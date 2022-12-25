n=int(input('enter the number:'))
a=-1
b=1
s=0
for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    s=s+c
print(s)
