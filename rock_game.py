import random
rock=''' ⭕'''
paper='''🛑 '''
scissor=''' ❌'''
game_image= [rock,paper,scissor]
user_choice=int(input("Enter your choice: Type 0 for Rock, for Papper, 2 for Scissor : ") )
if user_choice>=3 or user_choice<0:
    print(" You enterd invalid number, you lose.")
else:
    print(game_image[user_choice])
    computer_choice=random.randint(0,2)
    print("Computer choice: ")
    print(game_image[computer_choice])
    if computer_choice==user_choice:
         print("It's a draw 😎.")
    elif computer_choice>user_choice:
         print("Your Lose 🤩.")
    elif computer_choice<user_choice:
         print("you Win 🥳🏆.")
    elif computer_choice==0 and user_choice==2:
          print("Your Lose ❌❌")
    elif computer_choice==2 and user_choice==0:
         print("you Win 🥳🥉.")
#🥳🤩,🥳 ❌⭕🛑 🤩🥳🥉🏅🎖️🥇🥈🏆




    
