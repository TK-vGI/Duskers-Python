from config import TITLE, COMMANDS


def user_input() -> str:
    choice = input("Your command:\n")
    return choice


def play_game() -> None:
    print()

    user_name = input("Enter your name:\n")

    print()
    print(f"Greetings, commander {user_name}!")
    print("Are you ready to begin?\n\t[Yes] [No]")
    print()

    while True:
        answer = user_input().lower()
        if answer == "yes":
            print()
            print("Great, now let's go code some more ;)")
            break
        elif answer == "no":
            print()
            print(f"How about now.")
            print("Are you ready to begin?\n\t[Yes] [No]")
            print()
        else:
            print("Invalid input")
            print()

    return None


def main() -> None:
    print()
    for command in COMMANDS.values():
        print(command)
    print()

    while True:
        user_choice = user_input().lower()
        if user_choice not in COMMANDS:
            print("Invalid input\n")
        else:
            break

    match user_choice:
        case "exit":
            print("Thanks for playing, bye!")
            return None
        case "play":
            play_game()
        case _:
            print("Unknown command\n")

    return None


if __name__ == '__main__':
    print(TITLE)
    main()
