import random

wordList = ['ardvark', 'baboon', 'camel']

chosenWord = random.choice(wordList)

print(f"The chosen word is {chosenWord}")

display = []
for letter in chosenWord:
    display += "_"
print(display)

guess = input("Guess a letter: ").lower()

for position in range(len(chosenWord)):
    letter = chosenWord[position]
    if letter == guess:
        display[position] = letter
print(display)
