import random

def hangman():
    word_list = ["apple", "banana", "orange"]  # Replace with more words
    word = random.choice(word_list).lower()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display = ''.join(letter if letter in guessed_letters else '_' for letter in word)
        print(f"Word: {display}")
        
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word '{word}'.")
            break
    
    if attempts == 0:
        print(f"Sorry, you're out of attempts. The word was '{word}'.")

# Test the game
hangman()
