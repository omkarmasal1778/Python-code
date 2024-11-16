import random
'''a=random.randint(1,7)
b=random.randrange(1,3)
print(a)
print(b)
l=[4,56,-7,89]
random.shuffle(l)
print(l)
a=str(input("Enter anyone name"))
s=['omkar','Atharv','Kunal','Mahesh']
char=random.randint(a)
print(s)
if s:
    print(f"payment will pay by {a}")

t="Hi omkarooo"
s=t  .split("o")
print(s)'''
names=input("alls name: ")
name_list=names.split(",")
#ln=len(n_l)
#random.choice=random.randint(0,ln-1)
p_s=random.choice(name_list)
print(f"{random.choice(name_list)} will pay the bill")

