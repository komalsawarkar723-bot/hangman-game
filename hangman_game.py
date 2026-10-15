# CodeAlpha Internship - Task 1
# Hangman Game

import random

# List of 5 predefined words
words = ["python", "computer", "programming", "developer", "science"]

# Randomly select one word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 40)
print("        WELCOME TO HANGMAN GAME")
print("=" * 40)
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")
print()

# Create hidden version of the word
display_word = ["_"] * len(word)

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:

    # Display current word
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Take user input
    guess = input("Enter a letter: ").lower().strip()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        print()
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Try another one.")
        print()
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    # Check whether the letter is in the word
    if guess in word:
        print("Correct guess!")

        # Reveal the guessed letter
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1
        print("Wrong guess!")

    print()

# Game result
if "_" not in display_word:
    print("=" * 40)
    print("🎉 CONGRATULATIONS! YOU WON!")
    print("The word was:", word)
    print("=" * 40)

else:
    print("=" * 40)
    print("GAME OVER!")
    print("The correct word was:", word)
    print("=" * 40)