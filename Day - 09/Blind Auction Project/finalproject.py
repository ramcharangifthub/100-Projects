from art import logo
print(logo)
bids = {}

def find_highest_bidder(bidding_dictionary):
    winner = " "
    highest_bid = 0
    for bidders in bidding_dictionary:
        bidding_amount = bidding_dictionary[bidders]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidders
    print(f"The winners is {winner} with a bid of {highest_bid}")
should_continue = True
while should_continue:
    name = input("what is your name? \n")
    price = int(input("what is your price?\n$"))
    bids[name] = price
    should_continue = input("Do you want add any other bids?Type 'yes' or 'no': ")
    if should_continue == "no":
        find_highest_bidder(bidding_dictionary=bids)
        should_continue = False
    elif should_continue == "yes":
        print("\n" * 20)


