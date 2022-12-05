n=int(input('enter n number'))
L=n
S=n
for i in range(n):
    n=int(input('enter numbers'))
    if n>L:
        L=n
        if n<S:
            s=n
            print('the difference is',L-S)
            print('largest number is',L)
            print('smallest number is',S)
    
