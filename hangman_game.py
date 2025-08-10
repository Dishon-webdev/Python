import random

def hangman():
    words = ["python", "developer", "hangman", "computer", "programming", "dishon"]
    word = random.choice(words).upper()
    guessed = []
    tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("_ " * len(word))

    while tries > 0:
        guess = input("\nGuess a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry! '{guess}' is not in the word.")
            tries -= 1

        word_display = ""
        for letter in word:
            word_display += letter + " " if letter in guessed else "_ "

        print(display_hangman(tries))
        print(word_display)

        if "_" not in word_display:
            print("🎉 You win!")
            break
    else:
        print(f"💀 You lost! The word was {word}.")

def display_hangman(tries):
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / 
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |    
           |
        """,
        """
           ------
           |    |
           |    O
           |    
           |    
           |
        """,
        """
           ------
           |    |
           |    
           |    
           |    
           |
        """
    ]
    return stages[6 - tries]

if __name__ == "__main__":
    hangman()
