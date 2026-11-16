count=int(input("enter your no of items: "))
bill_total=0
for i in range(1,count+1):
    item_price=int(input("enter the item price"))
    bill_total=item_price+bill_total
print("total bill:",bill_total)