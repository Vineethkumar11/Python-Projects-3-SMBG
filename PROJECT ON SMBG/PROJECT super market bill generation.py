# PROJECT ON SUPER MARKET BILL GENERATION:
from datetime import datetime
name=input("Enter your name:")
lists='''
rice    Rs 20/kg
sugar   Rs 30/kg
salt    Rs 10/kg
oil     Rs 200/kg
daal    Rs 50/kg
powder  Rs 25/each
soap    Rs 45/each
perfume Rs 180/each
'''
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for items
items={'rice':20,'sugar':30,'salt':10,'oil':200,'daal':50,'powder':25,'soap':45,'perfume':180}
option=int(input('For list of items press 1-'))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy any items press 1 or 2 for exit-"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Please enter you items:")
        quantity=int(input('Enter quantity:'))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            GST=(totalprice*15)/100
            finalamount=GST+totalprice
        else:
            print('SORRY! YOU ENTERED ITEM ARE NOT AVAILBLE')
    else:
        print("WRONG NUMBER TRY AGAIN")
    inp=input("DO YOU WANT THE BILL yes or no:")
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*'~','VR SUPER MARKET',25*'~')
            print(28*'~','VGR,NELLORE',28*'~')
            print('Name:',name,30*' ','DATE:',datetime.now())
            print(70*" ")
            print('sno',15*' ',"items",15*' ','quantity',15*' ','price')
            
            for i in range(len(pricelist)):
                print(i,18*" ",ilist[i],20*" ",qlist[i],20*" ",plist[i])
            print(75*"-") 
            print('TotalAmount:','Rs',totalprice)
            print('GST amount:','Rs',GST)
            print(75*"-")
            print('FinalAmount:','Rs',finalamount)
            print(75*"-")
            print(20*" ",'THANKS FOR VISITING! SEE YOU AGIAN ',50*" ")
            print(75*"-")