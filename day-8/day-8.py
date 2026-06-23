from string import ascii_lowercase

LETTERS = list(ascii_lowercase)


def run_caesar_cipher():
    cipher_type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    while cipher_type != "encode" and cipher_type != "decode":
        print("That's not a valid cipher. Please try again.")
        cipher_type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    message = input(f"Type the message you want to {cipher_type}:\n")
    shift_num = input("Type the shift number:\n")
    while not shift_num.isnumeric():
        print("Please enter a valid number.")
        shift_num = input("Type the shift number:\n")
    shift_num = int(shift_num)
    if cipher_type == "encode":
        encoded_message = encode(message, shift_num)
        print(f"Here's the encoded result: {encoded_message}")
    else:
        decoded_message = decode(message, shift_num)
        print(f"Here's the decoded result: {decoded_message}")


def encode(message, shift):
    encoded_message = ""
    for letter in message:
        if letter == " ":
            encoded_message += letter
        new_letter_idx = LETTERS.index(letter) + shift
        if new_letter_idx > len(LETTERS) - 1:
            new_letter_idx = new_letter_idx - len(LETTERS)
        encoded_message += LETTERS[new_letter_idx]
    return encoded_message


def decode(message, shift):
    decoded_message = ""
    for letter in message:
        if letter == " ":
            decoded_message += letter
        new_letter_idx = LETTERS.index(letter) - shift
        if new_letter_idx < 0:
            new_letter_idx = len(LETTERS) + new_letter_idx
        decoded_message += LETTERS[new_letter_idx]
    return decoded_message


def caesar_cipher():
    while True:
        run_caesar_cipher()
        while True:
            play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
            if play_again in {"yes", "no"}:
                break
            print("That's not a valid input. Please try again.")

        if play_again == "no":
            print("Goodbye")
            break


caesar_cipher()
