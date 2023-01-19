s=input()
n=len(s)
for i in range(n,-1,-1):
   # print(s[0:i])#without space
    for j in range(i):
        print(s[j],end=' ')
    print()
