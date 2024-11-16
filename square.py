import random
import math

def play_game():
    previous_number = None
    while True:
        if previous_number is None:
            number = random.randint(1, 100)
        else:
            print(f"Previous number: {previous_number}")
            choice = int(input("Do you want to answer the previous question? (1 for Yes, 0 for No): "))
            if choice == 1:
                number = previous_number
            else:
                number = random.randint(1, 100)
        
        print(f"Find the square root of: {number}")
        user_answer = float(input("Your answer: "))
        correct_answer = math.sqrt(number)

        if math.isclose(user_answer, correct_answer, rel_tol=1e-5):
            print("Correct!")
            previous_number = None
        else:
            print(f"Incorrect! The correct answer was: {correct_answer:.5f}")
            previous_number = number

play_game()
