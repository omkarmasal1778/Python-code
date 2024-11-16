#import random
#a=random.randint(1,10) # 1 and 10 both arte include
#a=random.randrange(1,10) # 10 not include
#a=random.random()#0.7444179067361208
#a=random.uniform(1,10) 8.842140969264634
'''l=[2,34,53,67,78]
a=random.choice(l)

print(a)

side=random.randint(0,1)
print(side)
if side==1:
   print("Head")
else:
    print("Tails")'''
import random
name=input("Enter name :  ")
name_list=name.split(",")
length=len(name_list)
random_choice=random.randint(0,length-1)
print(f"{name_list[random_choice]} wil pay bill")