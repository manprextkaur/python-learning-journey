my_card={"name":"Aman",
         "Roll no":234,
         "course":"BCA",
         "city":"Jalandhar",
         "marks":450}
for i in my_card:
    print(i,":",my_card[i])
my_card["marks"]=470
print("marks is updated:",my_card["marks"])