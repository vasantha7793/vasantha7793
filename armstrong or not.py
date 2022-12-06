n=int(input('enter a number'))
s=0
while(n!=0):
    r=n%10
    n=n//10
    s=s+(r*r*r)
if n==s:
   print('Armstrong')
else:
   print('not a Armstrong')
