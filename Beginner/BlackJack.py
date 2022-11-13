import random

cards = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11}
card_values = list(cards.values())

def get_random_pick():
    """Returns a random card from the Deck"""
    return random.choice(card_values)

def calculate_score(cards):
    return sum(cards)

play_flag = input("Do you want to play black jack? Y/N ").lower()

if play_flag == 'y':
    user_picks = []
    system_picks = []
    for _ in range(2):
        user_picks.append(get_random_pick())
    print(f"User cards are: {user_picks}, Current score: {calculate_score(user_picks)}")
    system_picks.append(get_random_pick())
    print(f"System first card is: {system_picks}")

    game_continue_flag = True

    while game_continue_flag:
        user_count = calculate_score(user_picks)
        system_count = calculate_score(system_picks)

        if user_count > 21 :
            if 11 in user_picks :
                entry = user_picks.index(11)
                user_picks = user_picks[:entry] + [1] + user_picks[entry + 1:]
                print(f"User cards are: {user_picks}, Current score: {calculate_score(user_picks)}" )
            else:
                print(f"Your count is {calculate_score(user_picks)}. You went over")
                print("You lose!")
                game_continue_flag = False
        elif user_count == 21:
            print(f"Your count is {user_count}. That's Black Jack. You've Won")
            game_continue_flag = False
        else:
            ind = input("Do you want to pick another card? Y/N ").lower()
            if ind == 'y':
                element = get_random_pick()
                user_picks.append(element)
                print(f"User cards are: {user_picks}")
                user_count += int(element)
                print(f"The Sum of your picks is: {user_count}")
            else:
                #user count is fixed
                #system to generate and get count
                while game_continue_flag:
                    sys_ele = get_random_pick()
                    system_picks.append(sys_ele)
                    system_count += int(sys_ele)
                    if system_count > 21:
                        print("You Win !")
                        print(f"Your cards are {user_picks} and cardcount is {user_count}")
                        print(f"System cards are {system_picks} and cardcount is {system_count}")
                        game_continue_flag = False
                    elif system_count > user_count:
                        print("You Lose")
                        print(f"Your cards are {user_picks} and cardcount is {user_count}")
                        print(f"System cards are {system_picks} and cardcount is {system_count}")
                        game_continue_flag = False
                    elif system_count == user_count:
                        print(f"Your cards are {user_picks} and cardcount is {user_count}")
                        print(f"System cards are {system_picks} and cardcount is {system_count}")
                        print("Draw")
                        game_continue_flag = False

