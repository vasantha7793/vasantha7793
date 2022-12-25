l=[]
n=int(input('enter size:'))
for i in range(n):
    x=int(input('enter elements:'))
    l.append(x)
print(max(l)-min(l))
