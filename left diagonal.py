n=int(input())
matrix=[]
sum=0
for i in range(0,n):
    i=[]
    for j in range(0,n):
        x=int(input())
        sum.append(x)
    for i in range(n):
        for j in range(n):
            if i==j:
                sum=sum+matrix[i][j]
                print(sum)
                        
