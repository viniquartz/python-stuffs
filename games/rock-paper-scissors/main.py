import logging
from random import randint
from os import system, name
from time import sleep

logger = logging.getLogger()
if logger.handlers:
    for handler in logger.handlers:
        logger.removeHandler(handler)
if logger.hasHandlers():
    logger.setLevel(logging.getLevelName("INFO"))
else:
    logging.basicConfig(
        level=logging.getLevelName("INFO"),
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# TO DO: How to improve that? I would like to return to function main.
def sub_menu():
    main()

def header():
    clear()
    print("rock paper scissors game\n")

def menu():
    option_menu = True
    while option_menu == True:
        header()
        print("play\nexit\n")
        choice = input("/ ").lower()
        if choice == 'exit':
            exit(1)
        elif choice == 'play':
            option_menu = False
        else:
            print("invalid option!")
            sleep(2)
            continue
    return option_menu

def round_player_input():
    player = input("rock, paper or scissors? ")
    return player

def round_computer(options):
    computer = options[randint(0,2)]
    return computer

def win_lose_print(player, computer, winner):
    message = ""
    if winner == 'win':
        message = f"You win!! {player} wins against {computer}"
    else:
        message = f"You lose!! {computer} wins against {player}"
    print(message)
    return message

def main():
    options = ["rock", "paper", "scissors"]
    winner = menu()
    win_player = 0
    win_computer = 0
    round_results = []

    while winner == False:
        header()
        try:
            rounds = int(input("best of how many rounds(integer and odd)? "))
        except ValueError:
            print("invalid option!")
            sleep(1)
            continue
        for round in range(rounds):
            header()
            player = round_player_input()
            computer = round_computer(options)
            if player == computer:
                print("tie!")
                sleep(2)
                # TO DO: Repeat the round until computer or player win
                continue
            elif player == options[0]:
                if computer == options[1]:
                    round_results.append(win_lose_print(player, computer, "lose"))
                    win_computer+=1
                else:
                    round_results.append(win_lose_print(player, computer, "win"))
                    win_player+=1
            elif player == options[1]:
                if computer == options[2]:
                    round_results.append(win_lose_print(player, computer, "lose"))
                    win_computer+=1
                else:
                    round_results.append(win_lose_print(player, computer, "win"))
                    win_player+=1
            elif player == options[2]:
                if computer == options[1]:
                    round_results.append(win_lose_print(player, computer, "lose"))
                    win_computer+=1
                else:
                    round_results.append(win_lose_print(player, computer, "win"))
                    win_player+=1
            else:
                print("invalid option! lost the turn")
                sleep(1)
                # TO DO: Repeat the round until computer or player win
                continue
            rounds +=1
            sleep(2)
        winner = True
    header()
    print("Results:\n")
    for round_result in round_results:
        print(f"- {round_result}\n")
    print("\n\n")
    if win_player > win_computer:
        print(f"Congratulations!! You are the winner with {win_player} victories and computer with {win_computer}")
    else:
        print(f"No luck today!! computer with {win_computer} against {win_player} player")
    input()
    sub_menu()

if __name__ == "__main__":
    main()
