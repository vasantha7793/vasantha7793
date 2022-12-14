Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n=int(input())
... l=list(map(int,input().split()))
... min=l[0]
... max=l[0]
... for i in range(1,n):
...     if l[i]<min:
...         min=l[i]
...     if l[i]>max:
...         max=l[i]
... print(min)
