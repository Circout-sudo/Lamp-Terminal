import random
import os


def hangman():
    os.system("cls")
    with open('words.txt', 'r') as iot:
        word_list = iot.readlines()

    # Select a random word from the list
    word = random.choice(word_list).strip()
    # Use a set to store the letters the user has guessed
    letters_guessed = set()
    # Set the number of guesses the user has
    num_guesses = 18

    # Create a list of underscores the same length as the word
    # to represent the letters the user has not yet guessed
    word_letters = ["_" for _ in range(len(word))]

    # Main game loop
    while num_guesses > 0:
        # Print the current state of the word
        print("Current word: ", " ".join(word_letters))
        # Prompt the user to guess a letter
        letter = input("Guess a letter: ").lower().strip()
        # Check if the letter has already been guessed
        if letter in letters_guessed:
            print("You already guessed that letter.")
            continue
        # Add the letter to the set of letters guessed
        letters_guessed.add(letter)
        # Check if the letter is in the word
        if letter in word:
            print("Correct!")
            # Update the state of the word to reveal the letter
            for i in range(len(word)):
                if word[i] == letter:
                    word_letters[i] = letter
            # Check if the user has won
            if "".join(word_letters) == word:
                print("Congratulations, you won!")
                return
        else:
            print("Incorrect!")
            num_guesses -= 1
        print("You have", num_guesses, "guesses left.")
    # The user has run out of guesses
    print("You lost! The word was", word)

    def again():
        play_again = input("Do you want to play again?(Y/n)")
        if play_again == "y":
            hangman()
        elif play_again == "n":
            exit()
        else:
            print("Did not understand what your are trying to say")
            again()

    again()


hangman()
