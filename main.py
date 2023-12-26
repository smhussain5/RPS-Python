from pyfiglet import Figlet
import random

fig = Figlet(font="isometric1")  # WELCOME SCREEN
print(fig.renderText("RPS"))
print("WELCOME TO ROCK PAPER SCISSORS!")

game_choices = {  # GAME RULES
    1: "ROCK",
    2: "SCISSORS",
    3: "PAPER"
}

winning_sets = [(1, 2), (2, 3), (3, 1)]  # (user_choice, cpu_choice)

play_again = True  # GAME LOOP

while play_again:

    print("\n")  # GAME MENU
    print("Enter '1' for ROCK")
    print("Enter '2' for SCISSORS")
    print("Enter '3' for PAPER")
    print("\n")

    user_choice = int(input("What's your move?: "))  # GAME LOGIC
    cpu_choice = random.randint(1, 3)
    match_tuple = (user_choice, cpu_choice)

    print("\n")
    print(f"You chose {game_choices[user_choice]}")
    print(f"CPU chose {game_choices[cpu_choice]}")
    print("...")

    if user_choice == cpu_choice:
        print("GAME TIE!")
    elif match_tuple in winning_sets:
        print(f"{game_choices[user_choice]} BEATS {game_choices[cpu_choice]}")
        print("YOU WON!")
    else:
        print(f"{game_choices[cpu_choice]} BEATS {game_choices[user_choice]}")
        print("YOU LOSE!")

    replay_choice = input("Play again? Enter Y/N...: ")  # GAME REPLAY

    if replay_choice.upper() == "Y":
        play_again = True
    else:
        play_again = False

print("Thanks for playing! See you again next time!")  # GAME END
