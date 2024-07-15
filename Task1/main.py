import random

def hangman1(incorrect_guesses):
    stages = ["""
                  -----
                  |   |
                      |
                      |
                      |
                      |
                ---------
                """,
                """
                  -----
                  |   |
                  O   |
                      |
                      |
                      |
                ---------
                """,
                """
                  -----
                  |   |
                  O   |
                  |   |
                      |
                      |
                ---------
                """,
                """
                  -----
                  |   |
                  O   |
                 /|   |
                      |
                      |
                ---------
                """,
                """
                  -----
                  |   |
                  O   |
                 /|\\  |
                      |
                      |
                ---------
                """,
                """
                  -----
                  |   |
                  O   |
                 /|\\  |
                 /    |
                      |
                ---------
                """,
                """
                  -----
                  |   |
                  O   |
                 /|\\  |
                 / \\  |
                      |
                ---------
                """]
    print(stages[incorrect_guesses])

def hangman():
    # List of words to choose from
    words = ["python", "codealpha", "programming", "game", "hangman"]
    word = random.choice(words)
    word_length = len(word)
    guessed_word = ["_"] * word_length
    incorrect_guesses = 0
    total_incorrect_guesses = 6
    guessed_letters = []

    print("Welcome to Hangman Game")
    print("You have", total_incorrect_guesses, "incorrect guesses allowed.")
    print(" ".join(guessed_word))

    while incorrect_guesses < total_incorrect_guesses:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)

        if guess in word:
            for i in range(word_length):
                if word[i] == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess.")
            hangman1(incorrect_guesses)

        print(" ".join(guessed_word))
        print(f"Incorrect guesses: {incorrect_guesses}/{total_incorrect_guesses}")
        
        if "_" not in guessed_word:
            print("Congratulations! You Won!!")
            break
    else:
        hangman1(incorrect_guesses)
        print("The Person has been hanged. You Lost.")
        print("The word which you could not guess was : ", word)

# Call the hangman function to start the game
hangman()
