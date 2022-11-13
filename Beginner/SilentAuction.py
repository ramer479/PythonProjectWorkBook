import os

from Logos.AllArt import *

def get_highest_bidder(ip_dict):
    #{"RRR":1200, "KGF":1250, "GFR":100}
    new_dict ={}
    val_list = list(ip_dict.values())

    max_val = max(val_list)

    for k, v in ip_dict.items():
        if ip_dict[k] == max_val:
            new_dict[k] = v
            print(new_dict)
    return new_dict


print("Welcome to the Game! ")
print(gavelLogo)
bids = {}
bid_flag = True

while bid_flag:
    name_ip = input("Input the name: ")
    bid_ip = int(input("Enter Bid Amount $"))

    bids[name_ip] = bid_ip

    repeat_ip = input("Are there any other bidders? Type 'yes or 'no ").lower()
    if repeat_ip == "no":
        high_bid = get_highest_bidder(bids)
        for k,v in high_bid.items():
            print(f"The highest bidders in the Auction is ${v} from Mr/Mrs.{k}")
        bid_flag = False
    elif repeat_ip == "yes":
        os.system("clear")





