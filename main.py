# Higher Lower Game, using Instagram Followers
import random
from game_data import data
from art import logo, vs


# Check's the user's answer against the two options and determines who has the higher follower count, and if the user
# is correct
def check_answer(opt_a, opt_b, answer):
    follower_count_a = opt_a['follower_count']
    follower_count_b = opt_b['follower_count']
    winner = ""
    user_choice = ""

    if follower_count_a > follower_count_b:
        winner = opt_a['name']
    else:
        winner = opt_b['name']

    if answer == "a":
        user_choice = opt_a['name']
    else:
        user_choice = opt_b['name']

    if user_choice == winner:
        return True
    else:
        return False


# Updates user's score
def update_score():
    return score + 1


def update_a(opt_a, opt_b):
    follower_count_a = opt_a['follower_count']
    follower_count_b = opt_b['follower_count']

    if follower_count_a > follower_count_b:
        return opt_a
    else:
        return opt_b


print(logo)
print("Instructions:")
print("You will be given two options to choose from. The goal is to guess which option has more Instagram followers ("
      "not using real follower counts). "
      "\nCorrect guesses add to your score, an incorrect guess will end the game. \nGood luck!\n")

score = 0
game_over = False
option_a = random.choice(data)
option_b = random.choice(data)

while not game_over:
    # If both A and B are the same, reassign B until they are different
    while option_a == option_b:
        option_b = random.choice(data)

    print(f"A: {option_a['name']}, a {option_a['description']} from {option_a['country']}")
    print(vs)
    print(f"B: {option_b['name']}, a {option_b['description']} from {option_b['country']}")

    user_input = input(f"Who has more Instagram followers, {option_a['name']} [A] or {option_b['name']} [B]: ").lower()

    while user_input != "a" and user_input != "b":
        user_input = input("Invalid input. Please choose A or B: ")

    if check_answer(option_a, option_b, user_input):
        score = update_score()
        print(f"Correct! Your current score is: {score}\n")
        option_a = update_a(option_a, option_b)
        option_b = random.choice(data)
    else:
        game_over = True
        print(f"Sorry, incorrect. Your final score is: {score}")
