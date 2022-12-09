n=int(input())
m=int(input())
for i in range(1,n+1):
    k=0
    for j in range(1,m+1):
        k=k+1
        print(k,end='')
        m=m-1
        print()
