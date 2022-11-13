import random
import string

def get_random_string(num):
    lst_letters = list(string.ascii_letters)
    random_str = ''
    for i in range(0,num):
        random_str = random_str+random.choice(lst_letters)
    return  random_str

def get_random_symbols(num):
    lst_sym = list(string.punctuation)
    random_sym = ''
    for i in range(0,num):
        random_sym = random_sym.__add__(random.choice(lst_sym))
    return  random_sym

def get_random_num(num):
    lst_num = list(string.digits)
    random_num = ''
    for i in range(0,num):
        random_num = random_num.__add__(random.choice(lst_num))
    return  random_num

print("Welcome to Password Generator! ")
ip_pswd_len = int(input("Please enter the desired password length: "))
ip_pswd_num = int(input("Please enter the desired numbers in password: "))
ip_pswd_sym = int(input("Please enter the desired symbols in password: "))


if (ip_pswd_sym + ip_pswd_num) > ip_pswd_len:
    print("Invalid parameters lengths")
else :
    easy_pass = get_random_num(ip_pswd_num) + get_random_symbols(ip_pswd_sym) \
                + get_random_string(ip_pswd_len -(ip_pswd_sym+ip_pswd_num))
    hard_pass = ""
    lst_2 = list(easy_pass)
    pst = random.shuffle(lst_2)
    print(''.join(lst_2))



