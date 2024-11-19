##Hangman Game##
• This is a simple implementation of the classic Hangman game in Python. The objective of the game is to guess a randomly chosen word by guessing one letter at a time, before running out of tries.

##Features:##
• Randomly selects a word from a predefined list of fruits and vegetables.
• Displays a visual hangman with each incorrect guess, providing a graphical representation of the game’s progress.
• Tracks the guessed letters to avoid repeated guesses.
• Limits the player to 6 incorrect guesses (tries).
• Displays the current state of the word after each guess, showing correctly guessed letters and underscores for the remaining letters.

##How it works:##
• The player is shown a word with underscores representing unguessed letters.
• The player guesses one letter at a time.
• If the letter is in the word, it gets revealed; if not, the player loses a try.
• The game continues until the word is fully guessed or the player runs out of tries.

##Hangman Stages:##
• The game shows the following stages based on the number of remaining tries:
• Full figure with a head, body, arms, and legs (game over).
• Missing one part (head, arms, or legs), each stage indicating how many tries are left.

##How to Play:##
• Run the script, and it will prompt you to guess a letter. The game will give feedback after each guess and show the current progress of the word. You need to guess all letters before you run out of tries!

