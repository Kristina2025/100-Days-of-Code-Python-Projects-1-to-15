from string import ascii_lowercase

LETTERS = list(ascii_lowercase)


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


def run_caesar_cipher():
    cipher_type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    while cipher_type not in {"encode", "decode"}:
        print("That's not a valid cipher. Please try again.")
        cipher_type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    message = input(f"Type the message you want to {cipher_type}:\n").strip().lower()
    shift_num = input("Type the shift number:\n")
    while not shift_num.isnumeric():
        print("Please enter a valid number.")
        shift_num = input("Type the shift number:\n")
    shift_num = int(shift_num)
    if cipher_type == "encode":
        encoded_message = cipher(message, shift_num)
        print(f"Here's the encoded result: {encoded_message}")
    else:
        decoded_message = cipher(message, -shift_num)
        print(f"Here's the decoded result: {decoded_message}")


def cipher(message, shift):
    encoded_message = ""
    shift = shift % len(LETTERS)
    for letter in message:
        if letter not in LETTERS:
            encoded_message += letter
            continue
        new_letter_idx = LETTERS.index(letter) + shift
        encoded_message += LETTERS[new_letter_idx]
    return encoded_message


caesar_cipher()
