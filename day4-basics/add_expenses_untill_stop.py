total=0
count=0
expenses_amount=float(input("enter your expenses amount:"))
while expenses_amount!=0:
    total=total+expenses_amount
    count=count+1
    expenses_amount=float(input("enter your expenses amount:"))
    print(total)
    print(count)
if count>0:
    average=total/count
    print(average)

