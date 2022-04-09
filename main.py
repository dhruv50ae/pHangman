import random

import listOfWords

chosenWord = random.choice(listOfWords.wordList)

lives = 6

print(f"The chosen word is {chosenWord}")

display = []
for letter in chosenWord:
    display += "_"
print(display)

endOfGame = False
while not endOfGame:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(len(chosenWord)):

        letter = chosenWord[position]

        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

        if letter == guess:
            display[position] = letter

    if guess not in chosenWord:
        print(f"You guessed {guess}, life lost")
        lives -= 1
        print(f"You have {lives} lives remaining. ")
        if lives == 0:
            endOfGame = True
            print("You lose.")

    print(display)

    if "_" not in display:
        endOfGame = True
        print("You win")
