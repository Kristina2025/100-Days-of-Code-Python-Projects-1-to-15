from random import randint
from ascii_art import rock, paper, scissors

art = [rock, paper, scissors]
hands = ["rock", "paper", "scissors"]


def game():
    player_hand_inpt = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
    while player_hand_inpt not in ("0", "1", "2"):
        player_hand_inpt = input("Stop fooling around. Type 0 for Rock, 1 for Paper, or 2 for Scissors.")
    player_hand_int = int(player_hand_inpt)
    computer_hand_int = randint(0, len(art) - 1)
    print("User chose:\n", art[player_hand_int])
    print("Computer chose:\n", art[computer_hand_int])
    player_hand, computer_hand = hands[player_hand_int], hands[computer_hand_int]
    if player_hand == computer_hand:
        print(f"It's a tie. We both chose {player_hand}.")
    elif (player_hand == "rock" and computer_hand == "scissors") or \
            (player_hand == "paper" and computer_hand == "rock") or \
            (player_hand == "scissors" and computer_hand == "paper"):
        print(f"You win! Your {player_hand} beats my {computer_hand}!")
    else:
        print(f"You lose! My {computer_hand} beats your {player_hand}!")


game()
