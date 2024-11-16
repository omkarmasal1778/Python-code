h=int(input('Enter height:'))
bill=0
if h>=3:
    print('can ride')
    age=int(input('Enter age:'))
    if age<12:
        bill=150
        print('p=500')
    elif age<=18:
        bill=250
        print('p=250')
    else:
        bill=500
        print('p=500')
        want_photo=input('do you want photo (Y/N)?')
        if want_photo=='yes'or want_photo=='not':
         bill=bill+50
        print(f"your total bill is {bill}")
else:
    print('cant ride')
print('bye!!!!')



        