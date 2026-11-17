
attemps=0
while attemps <3:
    pin=int(input("enter your password:"))
    attemps=attemps+1  
    if pin==7888:
     print("access granted")
     break;
    else:
     print("denied")
    if pin!=7888 and attemps==3:
       print("your card is blocked")
   
  
 



