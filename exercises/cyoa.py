"""EX06 - Choose Your Own Adventure."""
__author__ = "730544275"


player: str = ""


ICE_CREAM: str = "\U0000F366"
NAMED_CONSTANT: str = "\U00000000"


def main() -> None:
    """Entrypoint of our game program."""
    greet()
    points: int = 0
    proceed = int(input("Please type in the number to choose an option for how you want to proceed. 1 leads you out of the game, 2 takes you right to the quiz, and 3 gives you a list of the best ice cream on Franklin Street to enjoy while you are taking your quiz. "))
    if proceed == 1: 
        print(f"Goodbye, you earned {points} adventure points.")
        restart: str = input(ICE_CREAM + "Would you like to restart the quiz? (Answer Yes or No.) " )
        if restart == "Yes" or "yes":
            main()
        return ICE_CREAM
    if proceed == 2:
        quiz()
    if proceed == 3: 
        fav_ice_cream: str = str(input(f"Hey, {player}! Do you enjoy eating ice cream? (Answer Yes or No.) "))
        if fav_ice_cream == "Yes" or "yes":
            points = points + 5
            print(f"There are a lot of great spots on Franklin street to enjoy right by campus. I reccomend YoPo for frozen yogurt, Ben and Jerry's for a super sweet treat, or Insomnia Cookies for an ice-cream/cookie sandwich! You increased your adventure points to {points} for learning about ice cream nearby. Goodbye! ")
            restart: str = input(ICE_CREAM + "Would you like to restart the quiz? (Answer Yes or No.) " )
            if restart == "Yes" or "yes":
                main()
            return ICE_CREAM
        else:
            points = points + 2
            print(f"Sorry you do not like ice cream. There are a lot of other sweet options, such as boba at YaYa or cookies at Crumbl. Hope you find something yummy. Have a nice day! You increased your adventure points to {points} for reading about sweet treats. Goodbye!")
            restart: str = input(ICE_CREAM + "Would you like to restart the quiz? (Answer Yes or No.) " )
            if restart == "Yes" or "yes":
                main()
            return ICE_CREAM 
    print("Now, spin the wheel to increase your points by a bonus number!")
    import random
    wheel = random.randint(1, 10)
    points = points + wheel
    print(f"Your final number of adventure points is {points}. Thanks for playing!")

def greet() -> None:
    """A function that greets the player before the game."""
    player_name = str(input("What is your name? "))
    global player
    player = player_name
    print(f"Welcome, {player}, to the quiz! This silly quiz will tell you what ice cream flavor you are based on some of your qualities. ")


def quiz() -> None:
    """A function that gives the quiz itself in the function."""
    print("Now it is time to start the quiz. Please pick one statement that best describes you and type Yes next to it. Type No next to the other qualities that are not your choice. ")
    question_one: str = input("1: You enjoy the classics, whether it's music, clothing, cars, etc. ")
    question_two: str = input("2: You have a bubbly personality and others would describe you as outgoing. ")
    question_three: str = input("3: You are sort of mysterious and are a quieter person. ")
    question_four: str = input("4: You enjoy volunteering and are kind, always ready to make meaningful connections. ")
    question_five: str = input("5: You are always laughing and make the best out of life. ")
    if question_one == True:
        points = points + 5
        print(f"You are vanilla! Your adventure points have increased to {points} for playing. ")
        restart: str = input(ICE_CREAM + "Would you like to restart the quiz? (Answer Yes or No.) " )
        if restart == "Yes" or "yes":
            main()
    return ICE_CREAM
    if question_one == "Yes" or "yes":
        points = points + 5
        print(f"You are vanilla! Your adventure points have increased to {points} for playing. ")
        restart: str = input(ICE_CREAM + "Would you like to restart the quiz? (Answer Yes or No.) " )
        if restart == "Yes" or "yes":
            main()
    return ICE_CREAM
    if question_two == "Yes" or "yes":
        points = points + 5
        print(f"You are strawberry! Your adventure points have increased to {points} for playing. ")
        restart: str = input(ICE_CREAM + "Would you like to restart the quiz? (Answer Yes or No.) " )
        if restart == "Yes" or "yes":
            main()
    return ICE_CREAM
    if question_three == "Yes" or "yes":
        points = points + 5
        print(f"You are red velvet! Your adventure points have increased to {points} for playing. ")
        restart: str = input(ICE_CREAM + "Would you like to restart the quiz? (Answer Yes or No.) " )
        if restart == "Yes" or "yes":
            main()
    return ICE_CREAM
    if question_four == "Yes" or "yes":
        points = points + 5
        print(f"You are brownie batter! Your adventure points have increased to {points} for playing. ")
        restart: str = input(ICE_CREAM + "Would you like to restart the quiz? (Answer Yes or No.) " )
        if restart == "Yes" or "yes":
            main()
    return ICE_CREAM
    if question_five == "Yes" or "yes":
        points = points + 5
        print(f"You are chocolate chip cookie dough! Your adventure points have increased to {points} for playing. ")
        restart: str = input(ICE_CREAM + "Would you like to restart the quiz? (Answer Yes or No.) " )
        if restart == "Yes" or "yes":
            main()
    return ICE_CREAM
    

if __name__ == "__main__":
  main()