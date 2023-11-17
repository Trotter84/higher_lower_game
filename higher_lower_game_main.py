from os import system
import random
import higher_lower_game_art
from higher_lower_game_data import data

def clear(): 
    _ = system('clear')

def ran_data():
    random_number = random.randrange(0, len(data))
    return random_number

def play_game():
    is_user_winning = True
    user_score = 0
    used_data = []
    choice_A = ran_data()
    while is_user_winning is True:
        choice_B = ran_data()
        used_data.append(choice_A and choice_B)
        if choice_A == choice_B:
            choice_B = ran_data()
        if choice_A or choice_B in used_data:
            choice_B = ran_data()
        print(higher_lower_game_art.logo)
        if user_score > 0:
            print(f"   You're right! Current score: {user_score}")
        print(f"Compare A: {data[choice_A]['name']}, a {data[choice_A]['description']}, from {data[choice_A]['country']}.")
        # print(data[choice_A]['follower_count'])
        print(higher_lower_game_art.vs)
        print(f"Against B: {data[choice_B]['name']}, a {data[choice_B]['description']}, from {data[choice_B]['country']}.")
        # print(data[choice_B]['follower_count'])
        user_answer = input("Who has more followers? Type'A' or 'B': ").lower()
        if user_answer == 'a' and data[choice_A]['follower_count'] > data[choice_B]['follower_count']:
            choice_A = choice_B
            user_score += 1
            clear()
        elif user_answer == 'b' and data[choice_B]['follower_count'] > data[choice_A]['follower_count']:
            choice_A = choice_B
            user_score += 1
            clear()
        else:
            print(f"   Sorry, that's wrong. Final score: {user_score}")
            is_user_winning = False


clear()
while input("Would you like to play a game of Higher vs Lower? Type 'y' or 'n': ") == 'y':
    clear()
    play_game()


