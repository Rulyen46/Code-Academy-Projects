#Plays Rock/Paper/Scissors
from random import randint

#Player options for RPS
options = ["ROCK", "PAPER", "SCISSORS"]

#Win/Lose/Tie condition responses
message = {
  "tie": "Yawn it's a tie!",
  "won" : "Yay you won!",
  "lost" : "Aww you lost!"
}

#Shows player choice, computer choice, determines winner and prints condition response
def decide_winner(user_choice, computer_choice):
  print("You selected %s." % user_choice)
  print("The computer selected %s." % computer_choice)
  if user_choice == computer_choice:
    print(message["tie"])
  elif user_choice == options[0] and computer_choice == options[2]:
    print(message["won"])
  elif user_choice == options[1] and computer_choice == options[0]:
    print(message["won"])
  elif user_choice == options[2] and computer_choice == options[1]:
    print(message["won"])
  else:
    print(message["lost"])

#Prompts player for choice, forces input to UPPER, selects computer choice and picks winner
def play_RPS():
  user_choice = input("Enter Rock, paper or scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,2)]
  decide_winner(user_choice, computer_choice)

play_RPS()