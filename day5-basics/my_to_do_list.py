to_do_list=[]
for i in range(3):
    task=input("enter your task")
    to_do_list.append(task)
for i in range(len(to_do_list)):
    print(i+1 ,to_do_list[i] )