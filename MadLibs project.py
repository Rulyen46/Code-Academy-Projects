"""
This program will receive input from players and output a madlibs story!
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' \
Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the \
rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and \
dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print("Mad Libs has started!")
name = input("Enter your name: ")
adj_1 = input("Please enter an adjective: ")
adj_2 = input("Please enter an adjective: ")
adj_3 = input("Please enter an adjective: ")
verb = input("Please enter a verb: ")
n1 = input("Please enter a noun: ")
n2 = input("Please enter a noun: ")
animal = input("What is your favorite animal? ")
food = input("What is your favorite food? ")
fruit = input("What is your favorite fruit? ")
hero = input("Who was your favorite childhood superhero? ")
country = input("Given the opportunity, what country would you live in? ")
dessert = input("What is your favorite dessert? ")
year = input("What year were you born? ")

print(STORY % (name, adj_1, adj_2, animal, food, verb, n1, fruit, adj_3, name, hero, name, country, name, dessert,
      name, year, n2))
