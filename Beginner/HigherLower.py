from Logos.AllArt import Logos
from HigherLowerGameData import *
import random

lgo = Logos()
game_flag = True
score = 0


def get_random_game_data():
    """ Gives random game data """
    game_data = data
    return random.choice(game_data)


def get_statement(data_dict):
    return f" {data_dict['name']}, a {data_dict['description']} from {data_dict['country']}"


A = ""
B = get_random_game_data()
while game_flag:

    print(f"Welcome to the Game {lgo.get_art_HigherLowerlogo()}")
    A = B
    print(f"Compare A: {get_statement(A)}")
    print(lgo.get_art_vs())

    B = get_random_game_data()
    print(f"Compare B: {get_statement(B)}")

    user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

    print(f"==========>   A follower count {A['follower_count']}")
    print(f"==========>   B follower count {B['follower_count']}")
    if user_input == 'A' and A['follower_count'] > B['follower_count']:
        score += 1
        print(f"Your score is {score}")
    elif user_input == 'B' and B['follower_count'] > A['follower_count']:
        score += 1
        print(f"Your score is {score}")
    else:
        print(f"Game ended. Your score is {score}")
        game_flag = False
