size=input("What size pizza you want (s/m/l)? ") 
billl=0
if size=='S'or size=='s':
    bill+=100
    print("small pizza price is     100Rs.")
elif size=='M' or size=='m':
    bill+=200
    print("Medium Pizza price is 200 Rs.")
else:
    bill+= 300
    print("Large Pizza price is 300 Rs.")
    
    add_pepperoni=input('Do you want ex')
    if add_pepperoni=='Y'or add_pepperoni=='y':
     bill+=50
    print(f"Your bill is {bill}")
      else:
      print("can not ride")
print("bye")
