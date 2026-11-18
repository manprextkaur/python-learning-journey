marks=[]
for i in range(5):
    subject_marks=int(input("enter your subject marks"))
    marks.append(subject_marks)
total=sum(marks)
print("total marks is :",total)   
average=total/len(marks)
print("average is:",average)
print("highest marks is ",max(marks))
print("lowest marks is ",min(marks))
print(sorted(marks))
