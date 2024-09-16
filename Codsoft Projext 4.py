import random

CHOICE=["rock","paper","scissors"]
game_continue=True
print("INSTRUCTIONS:")
print("Rock beats Scissor , Scissor Beats Paper , Paper beats Rock")
print("Every Wins Score +1")
while game_continue:
    count = 0
    run = input("Do you Want to play a rock paper scissor game ? 'y' for yes , 'n' for no : ")
    if run == "y":
        user_choice=input("What do you choose?'rock','paper','scissors': ")
        print(f"user choice:{user_choice}")
        computer_choice =random.choice(CHOICE)
        print(f"computer choice:{computer_choice}")
        if user_choice=="rock"and computer_choice=="rock" or user_choice=="paper"and computer_choice=="paper" or user_choice=="scissors"and computer_choice=="scissors":
            print("It's Draw")
        elif user_choice == "rock" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "scissors" or user_choice == "scissors" and computer_choice == "rock":
            print("User Loses")
        elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "scissors" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "rock":
            print("User Wins")
            count+=1
        print(f"User Score :{count}")

    else:
        game_continue=False
