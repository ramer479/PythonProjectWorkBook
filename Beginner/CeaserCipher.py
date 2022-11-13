import string
from Beginner.Logos.CipherArt import logo

class InvalidInputException(Exception):
    def __init__(self, *args, **kwargs):
        default_message = 'This is a default message!'

        # if any arguments are passed...
        # If you inherit from the exception that takes message as a keyword
        # maybe you will need to check kwargs here
        if args:
            # ... pass them to the super constructor
            super().__init__(*args, **kwargs)
        else:  # else, the exception was raised without arguments ...
            # ... pass the default message to the super constructor
            super().__init__(default_message, **kwargs)

lst = list(string.ascii_lowercase)

def encode_word (word, num):
    op_str = ""
    for i in word:
        if i in lst:
            new_index = lst.index(i) + num
            if new_index > 25:
                new_index = new_index % 26
            op_str += lst[new_index]
        else :
            op_str += " "
    return op_str

def decode_word (word,num):
    num = num % 26
    op_str = ""
    for i in word:
        if i in lst:
            new_index = lst.index(i) - num
            if new_index > 25:
                new_index += 26
            op_str += lst[new_index]
        else:
            op_str += " "
    return op_str

if __name__ == "__main__":
    print(logo)
    end_flag = False
    while not end_flag :
        ip_enc_dec = input("Do you want to Encode or Decode? ").lower()
        word = input("Input the Phrase here: ").lower()
        cipher_num = int(input("Input the Cipher number here: "))

        if ip_enc_dec == "encode":
            encode_op = encode_word(word,cipher_num)
            print(f"The Encode Output to the word {word} is {encode_op}")
        elif ip_enc_dec == "decode":
            decode_op = decode_word(word,cipher_num)
            print(f"The Decode Output to the word {word} is {decode_op}")
        else:
            raise InvalidInputException("Invalid Argument: Type Either Encode Or Decode")

        repeat_response = input("Do you want to Try again-Y/N? ")
        if repeat_response == "N":
            end_flag = True

