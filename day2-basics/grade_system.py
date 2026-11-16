english=float(input("enter your marks of english:"))
maths=float(input("enter your marks of maths:"))
science=float(input("enter your marks of science:"))
total_marks=english+maths+science
percentage=total_marks/300*100
print("total marks of 3 subject:",total_marks)
print("percentage is :",percentage,"%")
if percentage>=90:
      print("grade A")
elif percentage>=75:
      print("grade B")
elif percentage>=60:   
      print("grade C")
elif percentage>=40:   
      print("grade D")   
else:
      print("fail")
  