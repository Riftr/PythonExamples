# While loop example - Guessing games

# Basic guessing game example
secret_word = "cat"
guess = ""

while guess != secret_word:
    guess = input("Enter guess: ")

print("You Win!")



# Gussing game with 3 tries
secret_word = "kitten"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You Win!")
