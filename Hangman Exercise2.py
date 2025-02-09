import random

# List of possible words to guess
words = ["computer", "python", "hangman", "teacher", "simple"]

# Randomly choose one of the words
secret_word = random.choice(words)

# Keep track of letters the player has guessed
guessed_letters = set()

# Total lives the player starts with
lives = 7

# Hangman stages from 7 lives down to 0 lives
hangman_stages = [
"""
+---+
    |
    |
    |
    |
====
""",  # 7 lives left
"""
+---+
 |  |
 O  |
    |
    |
====
""",  # 6 lives
"""
+---+
 |  |
 O  |
 |  |
    |
====
""",  # 5 lives
"""
+---+
 |  |
 O  |
/|  |
    |
====
""",  # 4 lives
"""
+---+
 |  |
 O  |
/|\ |
    |
====
""",  # 3 lives
"""
+---+
 |  |
 O  |
/|\ |
/   |
====
""",  # 2 lives
"""
+---+
 |  |
 O  |
/|\ |
/ \ |
====
"""   # 1 life (next incorrect guess -> game over)
]

# Function to create the display of guessed letters (underscores for unguessed)
def get_display_word(word, guessed):
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"
        display += " "  # Add spacing between letters/underscores
    return display.strip()

# Game loop
while lives > 0:
    # Display current hangman stage based on how many lives are left
    # Index should be (7 - lives), but it must not exceed the last index of hangman_stages
    print(hangman_stages[7 - lives])

    # Show the letters guessed so far
    current_display = get_display_word(secret_word, guessed_letters)
    print("Word to guess:", current_display)
    print(f"Lives remaining: {lives}")

    # Check if the whole word is guessed
    if "_" not in current_display:
        print("Congratulations! You guessed the word!")
        break

    # Prompt user for a guess
    guess = input("Guess a letter: ").lower()

    # Validate the guess (single letter, not already guessed)
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter A-Z.")
        continue
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    # Add the guess to guessed_letters
    guessed_letters.add(guess)

    # Check if guess is in the secret word
    if guess not in secret_word:
        lives -= 1
        print(f"Wrong guess! You lose a life.\n")
    else:
        print("Good guess!\n")

# If lives reach 0, the player loses
if lives == 0:
    print(hangman_stages[-1])  # Final stage
    print("Word to guess:", get_display_word(secret_word, guessed_letters))
    print("Sorry, you're out of lives! The word was:",secret_word)