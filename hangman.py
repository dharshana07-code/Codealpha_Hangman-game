import random

# Words with hints
word_data = {
    "python": "A popular programming language",
    "planet": "Earth is one of these",
    "library": "A place full of books",
    "diamond": "A precious stone",
    "doctor": "we visit when we are sick"
}


def choose_word():
    word = random.choice(list(word_data.keys()))
    return word, word_data[word]


def show_progress(word, guessed):
    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


def word_completed(word, guessed):
    for letter in word:
        if letter not in guessed:
            return False
    return True


def play_game():
    secret_word, hint = choose_word()

    guessed_letters = []
    wrong_attempts = 0
    max_attempts = 6
    hint_used = False

    print("=" * 40)
    print("          HANGMAN GAME")
    print("=" * 40)
    print("   Guess the hidden word!   ")
    print("Type '?' once if you need a hint.")
    print()

    while wrong_attempts < max_attempts:

        print("\nWord:")
        show_progress(secret_word, guessed_letters)

        print("Wrong Attempts:", wrong_attempts, "/", max_attempts)

        if guessed_letters:
            print("Guessed Letters:", ", ".join(sorted(guessed_letters)))

        guess = input("\nEnter a letter: ").lower().strip()

        if guess == "?":
            if not hint_used:
                print("\nHint:", hint)
                hint_used = True
            else:
                print("Hint already used.")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct! Keep guessing!!")
        else:
            wrong_attempts += 1
            print("Oops!Wrong guess!")

        if word_completed(secret_word, guessed_letters):
            print("\nCongratulations! You did it!!")
            print("You guessed the word:", secret_word)
            return

    print("\nGame Over!")
    print("The correct word was:", secret_word)


while True:
    play_game()

    choice = input("\nDo you want to play again? (yes/no): ").lower()

    if choice != "yes":
        print("\nThanks for playing!")
        break