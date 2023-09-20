
from hangman_art import logo
from hangman_art import stages
word_list = ['advark', 'baboon', 'camel']
import random

chosen_word = random.choice(word_list)
print(logo)
#print("chosen word is: ",chosen_word)

display = []

for _ in range(len(chosen_word)):
    display += '_'
print(display)


end_of_game = False
lives = 6
while not end_of_game:

   
        
    guessed = input("Enter the letter :\n").lower()

    if guessed in display:
        print("you have already guessed this letter")

    for position in range (len(chosen_word)) :
        if chosen_word[position] == guessed:
            display[position] = guessed
        
    if guessed not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"you have {lives} lives")
        if lives == 0:
            end_of_game = True
            print("you lose")

    print(display)



    if '_' not in display:
        end_of_game = True
        print("you win")
        print(f"the chosen word was: {chosen_word}")


