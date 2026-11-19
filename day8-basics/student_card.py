my_card={"name":"Aman",
         "Roll no":234,
         "course":"BCA",
         "city":"Jalandhar",
         "marks":450}
for key in my_card:
    print(key,":",my_card[key])
my_card["marks"]=470
print("-----------updated card----------")
for key in my_card:
    print(key,":",my_card[key])
