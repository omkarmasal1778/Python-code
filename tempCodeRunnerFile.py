import random
name=input("Enter name :  ")
name_list=name.split(",")
length=len(name_list)
random_choice=random.randint(0,len-1)
print(f"{name_list[random_choice]} wil pay bill")