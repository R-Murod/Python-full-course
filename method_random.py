# Date - 04/02/2023
# action - действие
# rock - камень
# paper - бумага
# scissors - ножница
# action - действие

import random

# x = random.randint(1, 6) - random int numbers between 1 and 6
# y = random.random() - random float numbers between 0 and 1
while True:
    possible_action = ["rock", "paper", "scissors"]
    user_action = input("Enter a choice (rock, paper or scissors):  ")
    computer_action = random.choice(possible_action)  # рандомно выбирает
    print(f"You choose {user_action}")
    print(f"Computer choose {computer_action}")

    if user_action == computer_action:
        print(f"Draw!!!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("You Win!!!")
        else:
            print("You Lost!!!")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("You Win!!!")
        else:
            print("You Lost!!!")
    elif user_action == "paper":
        if computer_action == "rock":
            print("You Win")
        else:
            print("You Lost")
    play_again = input("Play again? (y/n) ")
    if play_again != "y":
        break

# method shuffle
# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "M", "S", "R"]
# random.shuffle(cards)
# print(cards)
