# Higher Lower Game, using Instagram Followers
import random
from game_data import data
from art import logo, vs

print(logo)
print("Instructions:")
print("You will be given two options to choose from. The goal is to guess which option has more Instagram followers. "
      "\nCorrect guesses add to your score, an incorrect guess will end the game. \nGood luck!")

game_over = False

while not game_over:
    option_a = random.choice(data)
    option_b = random.choice(data)

    # If both A and B are the same, reassign B until they are different
    while option_a == option_b:
        option_b = random.choice(data)

    print(option_a)
    print(option_b)
    game_over = True
