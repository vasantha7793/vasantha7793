n=int(input())
l=list(map(int,input().split()))
x=int(input())
low=0
high=n-1
flag=0
mid=(low+high)//2
while high>=low:
    if x>1[mid]:
        low=mid+1
       elif x==1[mid]:
    flag=1
    break
else:
    high=mid-1
    mid=(low+high)//2
    if flag==1:
        print('element is found at',mid,'index locatiob')
    else:
        print('element not found')
