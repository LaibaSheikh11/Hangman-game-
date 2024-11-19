import random

def print_hangman(tries):
    stages = [
        """
        _______
        |       |
        |       O
        |      /|\\
        |      / \\
        |
        """,
        """
        _______
        |       |
        |       O
        |      /|\\
        |      / 
        |
        """,
        """
        _______
        |       |
        |       O
        |      /|\\
        |      
        |
        """,
        """
        _______
        |       |
        |       O
        |      /|
        |      
        |
        """,
        """
        _______
        |       |
        |       O
        |       |
        |      
        |
        """,
        """
        _______
        |       |
        |       O
        |       
        |      
        |
        """,
        """
        _______
        |       |
        |       
        |       
        |      
        |
        """
    ]
    return stages[tries]

def hangman():
    word_list = ['apple', 'banana','pear' , 'orange' , 'cherry', 'date', 'tangerine', 'grape' , 'carrot' , 'mango' , 'pineapple' , 'peach' , 'Apricot' , 'watermelon' , 'strawberries' , 'pomegranate']
    chosen_word = random.choice(word_list)
    display = ["_"] * len(chosen_word)
    guessed_letters = []
    tries = 6

    print("_______Welcome to Hangman!________")
    print(f"The word has {len(chosen_word)} letters: {' '.join(display)}")

    while tries > 0 and "_" in display:
        print(print_hangman(tries))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in chosen_word:
            print(f"Good job! '{guess}' is in the word.")
            guessed_letters.append(guess)
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = guess
        else:
            print(f"Oops! '{guess}' is not in the word.")
            guessed_letters.append(guess)
            tries -= 1

        print(f"Word: {' '.join(display)}")
        print(f"Remaining tries: {tries}")

    if "_" not in display:
        print("Congratulations! You guessed the word!")
    else:
        print(print_hangman(0))
        print(f"Sorry, you ran out of tries. The word was '{chosen_word}'.")

if __name__ == "__main__":
    hangman()
