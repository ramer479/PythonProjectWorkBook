import random
from Utils.RandomUtils import RandomUtils

EASY_TURNS = 10
HARD_TURNS = 5

class InvalidArgumentsException(Exception):
    pass

def game_level_lives(level):
    if level == "easy":
        return EASY_TURNS
    elif level == "hard":
        return HARD_TURNS
    else :
        raise InvalidArgumentsException("Invalid argument. Please enter values - Easy/Hard")

def game():
    obj = RandomUtils()
    system_guess = obj.get_random_integer(strt_num=1, end_num=101)
    #print(f"The System Guess is {system_guess}")
    # Get the Game level from Cmd and assess the lives
    print("I'm thinking of number between 1 to 100")
    game_level = input("How do you like the Game level.Easy/Hard? ").lower()
    lives = game_level_lives(game_level)

    game_flag = True

    while game_flag:
        user_guess = int(input("Guess the number between 1 to 100: "))

        if user_guess == system_guess:
            print(f"You've won. The number {user_guess} guessed is Correct")
            game_flag = False
        else:
            if user_guess < system_guess:
                print(f"Too Low. Guess again! ")
            elif user_guess > system_guess:
                print(f"Too High. Guess again! ")
            lives = lives - 1
            print(f"You've {lives} left")
            if lives <= 0:
                print("You're out of Lives. You've lost. Please try again !")
                game_flag = False

game()




