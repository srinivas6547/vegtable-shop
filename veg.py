#Inventory

veg=['brinjal','ladyfinger','tomato','beens','potato','carrot','cucumber','bitterguard']
quantity=[15,12,20,10,20,8,14,6]
cost_price=[25,20,15,35,25,40,15,30]
sell_price=[30,25,17,38,28,43,16,37]
basket=[]
price=[]
max_qty=[]
print('*'*20,'STOCK AVAILABLE HERE','*'*20)
for s in zip(veg,quantity):
    print(s)
#Transaction
sum=0
base_fare=0
while True:
    item=input('which vegetable you want:')
    if item in veg:
        qty=float(input('how much quantity you want:'))
        idx=veg.index(item)
        if qty<=quantity[idx]: 
            amount=qty*sell_price[idx]
            actual_amount=qty*cost_price[idx]
            quantity[idx]=quantity[idx]-qty
            sum=sum+amount
            base_fare=base_fare+actual_amount
            basket.append(item)
            price.append(amount)
            max_qty.append(qty)
        else:
            if quantity[idx]>0:
                print('The stock available is only',quantity[idx],'kgs')
                print('out of stock')
            else:
                print('out of stock')

    else:
        print(item,'is not Availble')
    more=input('you want to buy another item(yes/no):')
    if more=='no':
        bill=input('you want to make the bill(yes/no):')
        if bill=='yes':
            for total_basket in zip(basket,price):
                print(total_basket)
            print('-'*8,'amount_payble=',sum,'-'*8)
            var=input('you want to close the shop(yes/no):')
            if var=='yes':
                print('*'*25,'Report','*'*25)
                for stock in zip(veg,quantity):
                    print(stock)
                x=max(max_qty)
                idx2=max_qty.index(x)
                y=basket[idx2]
                print('Today highest sold vegetable:',y,'--',x,'kgs')
                print('Today total profit is:',sum-base_fare)
                break