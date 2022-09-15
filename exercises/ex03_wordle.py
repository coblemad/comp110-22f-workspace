"""EX03 - Structured Wordle"""
__author__ = "730544275"

answer = "codes"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
def contains_char (guess_word: str, guess_character: str) -> bool:
    """A function that searches for a character in a word given by the user."""
    assert len(guess_character) == 1
    i = 0
    while i < len(guess_word):
        if guess_character == guess_word[i]:
            return True
        i += 1
    return False


def emojified (guess_word: str, answer: str) -> str:
    """A funciton that prints boxes for correct and incorrect guesses."""
    assert len(guess_word) == len(answer)
    i = 0
    result = ""
    while i < len(guess_word):
        if contains_char(answer, guess_word[i]) == True and guess_word[i] == answer [i]:
            result += GREEN_BOX
        else:
            if contains_char(answer, guess_word[i]) == True and guess_word[i] != answer[i]:
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        i += 1
    return result

def input_guess (expected_length: int) -> str:
    """A function that checks a word for the length given a certain amount of characters."""
    guess_word: str = input(f"Enter a {expected_length} letter word: ")
    while len(guess_word) != expected_length:
        if len(guess_word) > expected_length or len(guess_word) < expected_length:
            guess_word = input(f"That wasn't {expected_length} chars! Try again. ")
    return guess_word

def main() -> None: 
    """The entrypoint of the program and main game loop."""
    answer: str = "codes"
    guess_word: str = " "
    count: int = 1
    while guess_word != answer: 
        print(f"=== Turn {count}/6 ===")
        guess = input_guess(len(answer))
        print(emojified(guess_word, answer))
        if count <= 6 and guess_word != answer:
            count += 1
        if count >= 1 and guess_word == answer:
            print(f"You won in {count} turns! ")
            guess_word = answer
        if count == 7:
            print("X/6 - Sorry, try again tomorrow! ")

if __name__ == "__main__":
    main()