import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
end_of_the_game = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"
print(f" ".join(display))
while not end_of_the_game:
    guess = input("Guess a letter: ").lower()
    #Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        if chosen_word[position] == guess:
            display[position] = guess
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_the_game = True
            print("You lose.")
    
    if not "_" in display:
        end_of_the_game = True
        print("You win.")

    print(stages[lives])