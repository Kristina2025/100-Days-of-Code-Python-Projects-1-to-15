import random
from word_list import hangman_words as words
from ascii_art import hangman_logo as logo, hangmans
TOTAL_LIVES = 6
ALL_WORDS = [word for word_list in words.values() for word in word_list]


def play_game(word):
    print(logo)
    hangman_idx = 0
    hidden_word = ["_"] * len(word)
    print(f"Word to guess: ", "".join(hidden_word))
    print(word)

    lives_left = TOTAL_LIVES
    characters_to_guess = set(word)
    all_guesses = set()

    while lives_left > 0:
        guess = input("Guess a letter: ").lower()
        if guess in all_guesses:
            print("You already guessed that letter. Please try another one:")
            continue
        all_guesses.add(guess)

        if guess in characters_to_guess:
            characters_to_guess.remove(guess)

            for idx, letter in enumerate(word):
                if guess == letter:
                    hidden_word[idx] = letter

            print("".join(hidden_word))
            print(hangmans[hangman_idx])
            if not characters_to_guess:
                print("Congratulations, you won!")
                return
        else:
            lives_left -= 1
            hangman_idx += 1
            print(hangmans[hangman_idx])
            print(f"You guessed {guess}. That's not in the word. You lose a life!")
        if lives_left:
            print(f"{"*"*25}{lives_left}/{TOTAL_LIVES}LIVES LEFT{"*"*25}")
    print(f"{"*"*25}IT WAS {word}! YOU LOSE!{"*"*25}")


def choose_word():
    category = choose_category()
    if category:
        return random.choice(words[category])
    return random.choice(ALL_WORDS)


def choose_category():
    categories = " - ".join(words.keys())
    pick_category = input(f"Please choose a category: {categories}\n"
                          f"Or simply press enter and we'll choose a word for you.\n")
    if not pick_category:
        return None
    while pick_category not in words and pick_category != "":
        pick_category = input(f"Sorry, but that's not a valid a category.\n"
                              f"Please pick one from this list: {categories}\n"
                              f"Or press enter and we'll choose a word for you.\n")
    return pick_category


chosen_word = choose_word()
play_game(word=chosen_word)




