import random
import turtle

rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''



if __name__ == "__main__":

    print("Welcome to Rock, Paper & Scissors! ")
    user_choice = int(input("Choose your move from Rock-0, Paper-1, Scissors-2: \n"))

    if user_choice >= 3 or user_choice < 0:
        print("Your Move is invalid, Try Again !")
        user_choice = int(input("Choose your move from Rock-0, Paper-1, Scissors-2: \n"))
    game_list = [rock,paper,scissors]

    print("Your choice: \n"+game_list[user_choice])

    system_choice = random.randint(0,2)

    print("System choice: \n" + game_list[system_choice])

    if user_choice == system_choice :
        print("Its a Draw ! Play again")
    elif user_choice ==0 and system_choice == 2:
        print("You win!")
    elif user_choice == 2 and system_choice == 0:
        print("You Lose!")
    elif user_choice < system_choice:
        print("You Lose!")
    elif user_choice > system_choice:
        print("You Win!")

