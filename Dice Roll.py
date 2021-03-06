#User picks a number, computer rolls dice and determines a winner based on who has the higher number
from random import randint
from time import sleep

#Prompts user for a guess and stores the integer in a variable.
def get_user_guess():
  guess = int(raw_input("Please pick a number: "))
  return guess

#Rolls two dice, displays the values, then determines winner by highest number.
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print("The maximum number the computer can roll is %d." % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print("That number is too big. Please pick again.")
  else:
    print("Rolling...")
    sleep(2)
    print("The first roll is %s!") % first_roll
    sleep(1)
    print("The second roll is %s!") % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print("The computer rolled %s!") % total_roll
    sleep(1)
    if guess > total_roll:
      print("You have won!")
    else:
      print("You lost. Please play again.")
roll_dice(6)
