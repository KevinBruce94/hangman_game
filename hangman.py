import random
from hangman_words import word_list
from hangman_art import stages, logo

#create constants
word_list = word_list
game_over = False
lives = 6

#Create random word
chosen_word = random.choice(word_list)
# to see the word delete the '#' at the beginning of both lines
# print(chosen_word)

#Create an empty list to add an underscore for each letter in chosen_word
display = []
w_length = len(chosen_word)
for _ in range(w_length):
    display.append("_")

print(logo)

while not game_over:
    #Ask user for imput and make sure its always lowercase
    guess = input("Guess a letter: ").lower()

    #If the user guessed correctly their letter will replace the "_" at the correct position
    if guess in chosen_word:
        for position in range(w_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    elif guess not in chosen_word:
        print(f"Letter: '{guess}' was not correct. Try again..")
        lives -= 1
        print(f"{lives} lives left.")
        if lives == 0:
            game_over = True
            print("You lose.")
            print(f"The correct word was: {chosen_word}\n")


    print(f"{''.join(display)}")

    #Show the score with the correct guesses
    # print(display)
    if "_" not in display:
        print("You guessed the right word. You've won!")
        game_over = True

    print(stages[lives])


