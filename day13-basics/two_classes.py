python={"Aman","Ram","Kam","Lin"}
math={"Ram","Man","Lin","Kam"}
union=python|math
intersection=python&math
difference=python-math
print("Student in both classes:",sorted(union))
print("Student common in both classes:",sorted(intersection))
print("Student in python classes:",sorted(difference))