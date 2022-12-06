n=int(input('enter a number:'))
while(n!=0):
    r=n%10
    n=n//10
    if(n==r):
        print('palindrome!')
    else:
        print('not a palindrome!')
