import random
from Logos.HangManArt import hangmanLogo
dash_str = ""


def random_word_from_list():
    lst = ["kamu", "navya", "hemanth", "manohari", "raghu", "padmavathi", "suryakala", "prasanna"]
    return random.choice(lst)


def replace_str_index(text, index=0, replacement=''):
    return '%s%s%s' % (text[:index], replacement, text[index + 1:])


def get_position_list(c,s):
    lst = []
    for pos, char in enumerate(s):
        if (char == c):
            lst.append(int(pos))
    return lst


if __name__ == "__main__":
    print(hangmanLogo)

    print("Start Guessing. Pick one letter to Start!")

    target_word = random_word_from_list()
    print(target_word)

    for i in range(len(target_word)):
        dash_str += '_'
    chances = 6

    while chances > 0 and "_" in dash_str:
        input_letter = input("Type in the letter! => ")

        if input_letter in target_word :
            tm = get_position_list(input_letter, target_word)
            for i in tm:
                repl_str = replace_str_index(dash_str, i, input_letter)
                dash_str = repl_str
                print(f"@@@@{repl_str}")
        else:
            print(f"The num {input_letter} is not there. Please try again")
            chances -= 1
            print(f"The chances in if loop are {chances}")
            print(dash_str)


    if "_" not in dash_str and chances > 0:
        print("Yohooo! you win. You guessed it right")
    elif chances <= 0:
        print("Game Over! You lose")
