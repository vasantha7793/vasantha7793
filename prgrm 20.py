n=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(0,n,1):
    j=2
    flag=0
    while j<l[i]:
        if l[i]%j==0:
            flag=1
            break
        j=j+1
    if flag==0:
        p.append(l[i])
print(min(p))
print(max(p))
