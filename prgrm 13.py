n=int(input())
l=list(map(int,input().split()))
a=0
for i in range(n):
    for j in range(i+1,n):
        if l[i]==l[j]:
            a=1
            break
if a==1:
     print('list is duplicate')
else:
    print('List is unique')
