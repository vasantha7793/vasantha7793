empo=int(input('enter the empo:'))
empname=input('enter the empname:')
empdesig=input('enter the empdesig:')
basicsalary=int(input('enter the basicsalary:'))
da=int(input('enter the da:'))
ta=int(input('enter the ta:'))
hra=int(input('enter the hra:'))
netsalary=basicsalary+da+ta+hra
if netsalary>100000:
    tax=netsalary*10/100
    print('tax:',tax)
elif netsalary>50000:
    tax=netsalary*7/100
    print('tax:',tax)
elif netsalary>40000:
    tax=netsalary*4/100
    print('tax:',tax)
elif netsalary>20000:
    tax=netsalary*2/100
    print('tax:',tax)
else:
    print('tax=0')
