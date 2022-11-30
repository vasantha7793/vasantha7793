chocolates=150
blackgrams=200
dryfruits=500
potatochips=50
rice=1150
cphno=int(input('enter the phno:'))
name=input('enter the name:')
address=input('enter the address:')
chocolatesq=int(input('how many chocolates packets you want:'))
blackgramsq=int(input('how many blackgrams packets you want:'))
dryfruitsq=int(input('how many dryfruits packets you want:'))
potatochipsq=int(input('how many potatochips you want:'))
riceq=int(input('how many rice packets you want:'))
bill=(chocolates*chocolatesq)+(blackgrams*blackgramsq)+(dryfruits*dryfruitsq)+(potatochipsq*potatochips)+(rice*riceq)
if bill>3000:
    tax=bill*5/100
elif bill>2000:
    tax=bill*7/100
elif bill>1000:
    tax=bill*10/100
elif bill>500:
    tax=bill*15/100
else:
    tax=100
if cupon=='DIWALI'and bill>=5000:
    dis=bill*10/100
elif cupon=='DIWALI'and bill>=3000:
    dis=bill*6/100
elif cupon=='DIWALI'and bill>=1000:
    dis=bill*5/100
elif cupon=='CHRISTMAS'and bill>=3000:
    dis=bill*20/100
elif cupon=='CHRISTMAS'and bill>=2000:
    dis=bill*10/100
elif cupon=='CHRISTMAS'and bill>=1000:
    dis=bill*5/100
else:
    dis=0
print('customer phone number:',cphno)
print('customer name:',name)
print('customer address:',address)
print('tax:',tax)
print('dis:',dis)
bill=tax+bill-dis
print('bill:',bill)
