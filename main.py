import random

wordList = ['ardvark', 'baboon', 'camel']

chosenWord = random.choice(wordList)

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

    print(display)

    if "_" not in display:
        endOfGame = True
        print("You win")
