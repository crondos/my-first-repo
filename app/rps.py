
valid_selections = ["rock", "paper", "scissors"]
while True:
    player_selection = input("Please select Rock, Paper, or Scissors: ").strip().lower()
    if player_selection in valid_selections:
        print(f"You chose: {player_selection}")
        break
    else:
        print(f"So close dude. Try again — type Rock, Paper, or Scissors.")

import random

computer_selection = random.choice(valid_selections)

print(f"The computer chose: {computer_selection}")

if player_selection == computer_selection:
    result = "TIE! Please try again"
elif (
    (player_selection == "rock" and computer_selection == "scissors") or
    (player_selection == "paper" and computer_selection == "rock") or
    (player_selection == "scissors" and computer_selection == "paper")
):
    result = f"You Win! Lets play again?"
else:
    result = "Lenny Wins! Lets play again?"

print(result)
