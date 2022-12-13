ap=[]
n=int(input('enter number of districts:'))
for i in range(n):
    x=input('enter district:')
    ap.append(x)
    ap.sort()
print(ap)
