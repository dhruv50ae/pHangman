import random

wordList = ['ardvark', 'baboon', 'camel']

chosenWord = random.choice(wordList)

print(f"The chosen word is {chosenWord}")
guess = input("Guess a letter: ").lower()

for letter in chosenWord:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
