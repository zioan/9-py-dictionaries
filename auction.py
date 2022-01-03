import os
bids = []

auction_end = False

while not auction_end:
    name = input("What is your name?: ")
    amount = int(input("What is your bid?: $"))
    bidder = {"name": name, "amount": amount}
    bids.append(bidder)
    auction_continue = input("Are there any onther bidders? 'y'/'n': ")
    os.system('cls')
    if auction_continue == "n":
        auction_end = True

max_bid = 0
winner = ""
for bidder in bids:
    if max_bid < bidder["amount"]:
        winner = bidder["name"]
        max_bid = bidder["amount"]

print(f"The winner is {winner} with a bid of ${max_bid}!")
