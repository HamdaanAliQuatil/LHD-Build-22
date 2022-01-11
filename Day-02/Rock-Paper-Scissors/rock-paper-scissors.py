import random
flag = "y"
while flag.lower() == "y":
    print("Choices:\n1 - Rock\n2 - Paper\n3 - Scissors")
    while True:
        user_action = int(input("Enter your choice: "))
        if user_action in [1,2,3]: break
        else: print("Please enter a valid choice i.e., 1, 2 or 3")
    user_action = {1:"rock", 2:"paper", 3:"scissors"}[user_action]
    computer_action = random.choice(["rock", "paper", "scissors"])
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    flag = input("Play again? (y/n): ")