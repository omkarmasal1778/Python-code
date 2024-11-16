'''row1=['😀', '😀','😀']
row2=['😀', '😀','😀']
row3=['😀', '😀','😀']

matrix=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")

position=input("Enter the position where you want hide mony :  ")
row_num=int(position[0])
column_num=int(position[1])

row_selected=matrix[row_num-1] #This assigns the selected row (which is a list) to the variable
row_selected[column_num-1]='🥰'

print(f"{row1}\n{row2}\n{row3}")
'''
num=[10,34,-6,79,95,-2,56]
#names=['rakesh','seeta','geeta','ram','om']
#print(num[0:2:1])
#num.append(45)
#num.insert(2,68)
#num.extend([1,2,3,4,5])
#num[1]=33
#num[0:5]=[1,2,3,4,5]
#num.remove(-6)
#num.count(2)
#print(num.copy())

print(num)
#mix_list=[1,23,'om',67,'ram',56]
#print(max(num))
#print(min(num))
#print(mix_list[-1:-4])