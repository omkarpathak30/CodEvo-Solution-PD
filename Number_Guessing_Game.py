import random

number = random.randint(1, 10)
attempts = 3  

while attempts > 0:
    guess = int(input(f"Guess a number between 1 and 10 (you have {attempts} attempts): \n"))
    
    if number == guess:
        print("Congratulations! You've guessed the number.")
        break
    elif number > guess:
        print("Too low!")
    else:
        print("Too high!")
    
    attempts -= 1

if attempts == 0 and number != guess:
    print(f"Sorry, you've used all your attempts. The number was {number}.")