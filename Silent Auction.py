import os
from Hammer_Art import judge_hammer
auction = {}
    
def get_the_winner(acution):
    winner_name = ""
    highest_bid = 0
    for name in auction:
        if auction[name] > highest_bid:
            winner_name = name
            highest_bid = auction[name]

    print(f"The winner is {winner_name} with ${highest_bid} bid.") 

print(judge_hammer) #ASCII ART

end_loop = False
while(not end_loop):
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))

    auction[name] = bid
    
    more_bidders = input('are there any other bidders? type "yes" or "no".').lower()

    if(more_bidders == "no"):
        end_loop = True
    os.system('cls')

get_the_winner(auction)