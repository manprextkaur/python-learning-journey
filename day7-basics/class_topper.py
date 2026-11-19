topper_total=0
topper_name=""
for i in range(4):
    student_name=input("enter your name:")
    marks=[]
    for j in range(5):
        student_marks=int(input("enter your marks:"))
        marks.append(student_marks)
    print("name is:",student_name)
    total=sum(marks)
    print("total marks is :",total)
    topper_name=student_name
    topper_total=total
    if topper_total>=450:
        print("topper is",topper_name,total)
print("topper is:",topper_name,topper_total)