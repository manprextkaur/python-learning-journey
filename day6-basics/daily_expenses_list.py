day_expense=[]
for i in range(5):
    expenses=int(input("enter you one day expense:"))
    day_expense.append(expenses)
total_spent=sum(day_expense)
print("total spent in a day:",total_spent)
average=total_spent/len(day_expense)
print("average spent per day:",average)
print("biggest expense in a day:",max(day_expense))
print("smallest expense in a day:",min(day_expense))
print(sorted(day_expense))