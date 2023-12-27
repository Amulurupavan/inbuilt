prices=[10,20,30,40]
new_price=[]
for price in prices:
    new_price.append(price+1)
    print(new_price)
    
    
prices=[10,20,30,40]
def add(price):
    return price+1

new_prices=list(map(add,prices))
print(new_prices)


prices=[10,20,30,40]
new_prices=list(map(lambda price:price+1,prices))
print(new_prices)