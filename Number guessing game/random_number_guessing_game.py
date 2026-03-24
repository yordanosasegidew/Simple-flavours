"""
Future improvement idea let the user first choose from different range of
numbers to switch the difficulty of the game and then play the game based 
on the selected difficulty level.
"""
import random 

print("\n===== RANDOM NUMBER GUESSING GAME =====\n")
print("HINT: 3 attempts from 1 to 50, only integers allowed")

def random_guess_game():
    floor_rand = 1
    ceiling_rand = 50
    attempts = 0
    user_guess = None
    rand_sel = random.randint(floor_rand,ceiling_rand)

    while attempts < 3:
        try:
            user_guess = int(input("Enter guess: "))

            if user_guess > ceiling_rand or user_guess < floor_rand:
                print("Out of bound")
            else:
                attempts += 1
                if user_guess < rand_sel:
                    print("TOO LOW, please try again !")
                elif user_guess > rand_sel:
                    print("TOO HIGH, please try again !")
                else:
                    print("YOU FOUND IT HIGH FIVE 🙌")
                    print(f"IT TOOK YOU {attempts} ATTEMPTS")
                    break
        except (ValueError):
            print("You can only put integers !!!")

    if attempts <= 3 and user_guess == rand_sel:
        print("GAME WON")
    else:
        print("GAME OVER")
        print(f"The number was:{rand_sel}")

while True:
    random_guess_game()
    while True:
        print("Want to play again?")
        answer = str(input("Yes/No (Y/N): "))

        if answer.lower() == 'y':
            print("TRYING AGAIN")
            break
        elif answer.lower() == 'n':
            print("QUITTING GAME")
            exit()
        else:
            print("INVALID INPUT")