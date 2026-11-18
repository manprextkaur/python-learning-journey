item_price=[]
for i in range(5):
    price=int(input("enter your price"))
    item_price.append(price)
total=sum(item_price)
print("total price is:",total)
average=total/len(item_price)
print("the average is:",average)
print("costliest price is:",max(item_price))
print("cheapest price is:",min(item_price))
print(sorted(item_price))
