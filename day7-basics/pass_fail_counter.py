pass_counter=0
fail_counter=0
for i in range(4):
    student_name=input("enter your name:")
    marks=[]
    for j in range(5):
        student_marks=int(input("enter your marks:"))
        marks.append(student_marks)
    print("name is:",student_name)
    total=sum(marks)
    print("total marks is :",total)
    percentage=total/500*100
    if percentage>=40:
        print("Pass")
        pass_counter=pass_counter+1
   
    else:
        print("fail")
        fail_counter=fail_counter+1
print("fail",fail_counter)
print("pass:",pass_counter)
    
    