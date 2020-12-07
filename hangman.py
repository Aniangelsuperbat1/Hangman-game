import random
from words import words

word = random.choice(words)

allowed_errors = 2
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")

    guess = input(f"allowed guesses left {allowed_errors}, next guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break 
    
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False


