from ascii_art import logo


def auction():
    print(logo)
    bids = {}
    while True:
        name = input("What is your name?: ")
        bid = input("What is your bid?: $")
        while not bid.isnumeric():
            print("That's not a valid bid. Please try again")
            bid = input("What is your bid?: $")

        bids[name] = int(bid)

        keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
        while keep_bidding not in {"yes", "no"}:
            print("That's not a valid input. Please try again.")
            keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

        clear_screen()
        print(logo)

        if keep_bidding == "no":
            winner = get_bid_winner(bids)
            print(f"The winner is {winner} with a bid of ${bids[winner]}!")
            break


def get_bid_winner(bids):
    winner = None
    winning_bid = 0
    for bidder in bids:
        bid = bids[bidder]
        if bid > winning_bid:
            winning_bid = bid
            winner = bidder
    return winner


def clear_screen():
    print("\n"*50)


auction()
