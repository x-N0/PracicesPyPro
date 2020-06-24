import random

OPTIONS = ['rock', 'paper', 'scissors']


def print_options():
    print('\n'.join(f'({i}) {opt}' for i, opt in enumerate(OPTIONS)))


def get_username():
    return input("Chose your username> ")


def get_computer_opt():
    return OPTIONS[random.randint(0, len(OPTIONS) - 1)]


def get_user_choice():
    return OPTIONS[int(input("Enter the number of your choice: "))]


def print_choices(USER, user_choice, bot_choice):
    return print(f"{USER}:" + user_choice + "\n" + "BOT:" + bot_choice)


def base_case(user_choice, bot_choice, winable):
    if bot_choice == winable:
        return f"{USER} WON"
    else:
        return f"{USER} LOSE"


def match_winner(user_choice, bot_choice):
    OPTS = {"rock": base_case("rock", bot_choice, "scissors"),
            "paper": base_case("paper", bot_choice, "rock"),
            "scissors": base_case("scissors", bot_choice, "paper")}
    if user_choice == bot_choice:
        print("DRAW")
        return
    return print(OPTS[user_choice])

USER = get_username()
print_options()
user_choice = get_user_choice()
bot_choice = get_computer_opt()
print_choices(USER, user_choice, bot_choice)
match_winner(user_choice, bot_choice)
