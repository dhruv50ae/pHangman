import random

wordList = ['ardvark', 'baboon', 'camel']

chosenWord = random.choice(wordList)

lives = 6

print(f"The chosen word is {chosenWord}")

display = []
for letter in chosenWord:
    display += "_"
print(display)

endOfGame = False
while not endOfGame:

    guess = input("Guess a letter: ").lower()

    for position in range(len(chosenWord)):

        letter = chosenWord[position]

        # print(
        #     f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")

        if letter == guess:
            display[position] = letter

    if guess not in chosenWord:
        lives -= 1
        print(f"You have {lives} lives remaining. ")
        if lives == 0:
            endOfGame = True
            print("You lose.")

    print(display)

    if "_" not in display:
        endOfGame = True
        print("You win")
