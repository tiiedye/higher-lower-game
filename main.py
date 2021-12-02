# Higher Lower Game, using Instagram Followers
import random
from game_data import data
from art import logo, vs

print(logo)
print("Instructions:")
print("You will be given two options to choose from. The goal is to guess which option has more Instagram followers. "
      "\nCorrect guesses add to your score, an incorrect guess will end the game. \nGood luck!\n")

score = 0
game_over = False

while not game_over:
    option_a = random.choice(data)
    option_b = random.choice(data)

    # If both A and B are the same, reassign B until they are different
    while option_a == option_b:
        option_b = random.choice(data)

    print(option_a)
    print(option_b)

    print(f"A: {option_a['name']}, a {option_a['description']} from {option_a['country']}")
    print(vs)
    print(f"B: {option_b['name']}, a {option_b['description']} from {option_b['country']}")

    user_input = input(f"Who has more Instagram followers, {option_a['name']} [A] or {option_b['name']} [B]").lower()

    while user_input != "a" and user_input != "b":
        user_input = input("Invalid input. Please choose A or B:")

    game_over = True
