

if __name__ == "__main__":
    print("Welcome to Pizza Delivery")
    pizza_size_ind = input("What size of pizza, you'd like to order - S, M or L? ")
    pepperoni_ind = input("Would you like to add Pepporoni Y/N?  ")
    cheese_ind = input("Would you like to add extra cheese Y/N? ")

    bill = 0
    if pizza_size_ind == "L":
        bill += 25
    elif pizza_size_ind == "M":
        bill += 20
    elif pizza_size_ind == "S":
        bill += 15

    if pepperoni_ind == 'Y':
        bill += 5
    if cheese_ind == "Y":
        bill += 3

    print(f"Total bill: {bill}$")