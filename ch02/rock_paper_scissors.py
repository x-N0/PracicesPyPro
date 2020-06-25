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


def base_case(bot_choice, winable):
    if bot_choice == winable:
        return f"{USER} WON"
    else:
        return f"{USER} LOSE"


def match_winner(user_choice, bot_choice):
    # I would prefer to use numbers for the options since the beginning.
    OPTS = {"rock": base_case(bot_choice, "scissors"),
            "paper": base_case(bot_choice, "rock"),
            "scissors": base_case(bot_choice, "paper")}
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


# Wrapped version
class RockPaperScissorsSimulator:
    def __init__(self):
        self.bot_choice = None
        self.user_choice = None
        self.OPTIONS = ['rock', 'paper', 'scissors']

    def simulate(self):
        self.USER = input("CHOOSE AN USERNAME: ")
        self.print_options()
        self.bot_choice = self.get_computer_opt()
        self.user_choice = self.get_user_choice()
        self.print_choices()
        self.match_winner()

    def print_options(self):
        print('\n'.join(f'({i}) {opt}' for i, opt in enumerate(self.OPTIONS)))

    def get_computer_opt(self):
        return self.OPTIONS[random.randint(0, len(self.OPTIONS) - 1)]

    def get_user_choice(self):
        return self.OPTIONS[int(input("Enter the number of your choice: "))]

    def print_choices(self):
        return print(f"{self.USER}:" + self.user_choice + "\n" + "BOT:" + self.bot_choice)

    def base_case(self, winable):
        if self.bot_choice == winable:
            return f"{self.USER} WON"
        else:
            return f"{self.USER} LOSE"

    def match_winner(self):
        # I would prefer to use numbers for the options since the beginning.
        OPTS = {"rock": self.base_case("scissors"),
                "paper": self.base_case("rock"),
                "scissors": self.base_case("paper")}
        if self.user_choice == self.bot_choice:
            print("DRAW")
            return
        return print(OPTS[self.user_choice])


sim1 = RockPaperScissorsSimulator()
sim1.simulate()
