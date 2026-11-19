for i in range(3):
    student_name=input("enter your name")
    marks=[]
    for j in range(5):
        student_marks=int(input("enter your marks for each subject:"))
        marks.append(student_marks)
    total=sum(marks)
    print("total marks is:",total)
    percentage=total/500*100
    print("percentage is :",percentage)
    if percentage>=90:
        print("grade A")
        print("Pass")
    elif percentage>=75:
        print("grade B")
        print("Pass")
    elif percentage>=60:
        print("grade C")
        print("Pass")
    elif percentage>=40:
        print("grade D")
        print("Pass")
    else:
        print("fail")
    

