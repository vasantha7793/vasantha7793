n=int(input())
m=int(input())
k=0
for i in range(1,n+1):
    for j in range(1,i):
        print(k,end='')
        k=k+1
        m=m+1
        print()
