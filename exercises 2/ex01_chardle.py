"""EX01 - Chardle - A cute step toward Wordle."""
_author_ = "730544275"

word: str = str(input("Enter a 5-character word "))
if len(word) > 5:
    exit()
if len(word) < 5:
    exit()
character: str = str(input("Enter a single character "))
if len(character) > 1:
    exit()
if len(character) < 1:
    exit()
print("Searching for " + character + " in" + word)
count: int = 0
if character == word[0]:
    print(character + " found at index 0")
    count = count + 1
if character == word[1]:
    print(character + " found at index 1")
    count = count + 1
if character == word[2]:
    print(character + " found at index 2")
    count = count + 1
if character == word[3]:
    print(character + " found at index 3")
    count = count + 1
if character == word[4]:
    print(character + " found at index 4")
    count = count + 1
if count == 1:
    print(str(count) + " instance of " + character + " found in " + word )
if count == 0:
    print("No instances of " + character + " found in " + word )
if count > 1:
    print(str(count) + " instances of " + character + " found in " + word )