def find_total(marks):
    return sum(marks)
def find_percentage(total):
    return total/500*100
def find_grade(percent):
    if percent>=90:
        return "A"
    elif percent>=75:
        return "B"
    elif percent>=60:
        return "C"
    elif percent>=40:
        return "D"
    else:
        return "Fail"
marks=[80,60,70,99,89]
total=find_total(marks)
percent=find_percentage(total)
grade=find_grade(percent)
print("total marks is:",total)
print("percentage is:",percent)
print("grade is:",grade)