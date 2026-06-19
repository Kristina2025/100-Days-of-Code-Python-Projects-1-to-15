import random
from word_list import hangman_words as words
from ascii_art import hangman_logo as logo, hangmans
TOTAL_LIVES = 6


def game():
    print(logo)
    hangman_idx = 0
    all_words = list(words.values())
    word_category = choose_category()
    if not word_category:
        word = random.choice(random.choice(all_words))
    else:
        word = random.choice(all_words[word_category])
    hidden_word = ["_" for _ in range(len(word))]
    print(f"Word to guess: {"".join(hidden_word)}")
    print(word)
    total_guesses, letters_guessed = len(set(word)), 0
    lives_left = TOTAL_LIVES
    all_guesses = []
    while lives_left > 0:
        guess = input("Guess a letter: ")
        if guess in all_guesses:
            print("You already guessed that letter. Please try another one:")
            continue
        all_guesses.append(guess)
        if guess in set(word):
            letters_guessed += 1
            for idx, letter in enumerate(word):
                if guess == letter:
                    hidden_word[idx] = letter
            print("".join(hidden_word))
            print(hangmans[hangman_idx])
            if letters_guessed == total_guesses:
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


def choose_category():
    categories = " - ".join(words.keys())
    pick_category = input(f"Please choose a category: {categories}\n"
                          f"Or simply press enter and we'll choose a word for you.\n")
    if not pick_category:
        return None
    while pick_category not in list(words.keys()) and pick_category != "":
        pick_category = input(f"Sorry, but that's not a valid a category.\n"
                              f"Please pick one from this list: {categories}\n"
                              f"Or press enter and we'll choose a word for you.\n")
    return pick_category


game()




