"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730544275"

answer = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess: str = input("What is your 6-letter guess? ")
while len(guess) != len(answer):
    guess = (input("That was not 6 letters! Try again: "))
index_track = 0
emoji_result = ""
while index_track < len(answer):
    if guess[index_track] == answer[index_track]:
        emoji_result += GREEN_BOX
    else: 
        letter_exists = False
        alternate = 0
        while alternate < len(answer) and not letter_exists:
            if guess[index_track] == answer[alternate]:
                letter_exists = True
                alternate += 1
            else:
                alternate += 1
        if letter_exists:
            emoji_result += YELLOW_BOX
        else:
            emoji_result += WHITE_BOX
    index_track += 1
print(emoji_result)
if len(guess) == len(answer) and guess != answer:
    print("Not quite. Play again soon! ")
if guess == answer:
    print("Woo! You got it! ")