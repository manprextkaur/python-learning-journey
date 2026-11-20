def addition(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b
def modulus(a,b):
    return a%b
a=int(input("enter your number:"))
b=int(input("enter your number:"))
print("press 1 for addition operation")
print("press 2 for subtract operation")
print("press 3 for multiplication operation")
print("press 4 for division operation")
print("press 5 for modulus operation")
choice=int(input("enter the choice you want to perform operation"))
if choice==1:
        print("addition operation is perform:")
        result=addition(a,b) 
        print("result is:",result)                 

elif choice ==2:
    print(" subtract operation is perform:")
    result=subtract(a,b) 
    print("result is:",result) 


elif choice ==3:
    print(" multiplication operation is perform:")
    result=multiplication(a,b) 
    print("result is:",result) 
                               
                            
elif choice ==4:
    print(" division operation is perform:")
    result=division(a,b) 
    print("result is:",result) 
                               
                            
elif choice ==5:
    print(" modulus operation is perform:")
    result=modulus(a,b) 
    print("result is:",result) 
                               
else:
    print("choose correct option")

                        

                        


