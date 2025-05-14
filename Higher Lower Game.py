import random
from art import logo,vs
from game_data import data


# Generate First Value
def first_value():
    value=random.choice(data)
    result=f"{value['name']} A {value['description']} from {value['country']}"
    return result,value['follower_count']

# Generate Second Value
def second_value():
    value=random.choice(data)
    result=f"{value['name']} A {value['description']} from {value['country']}"
    return result,value['follower_count']

#Build Final Game Function
def final_game():
    user_score = 0
    value_1 = first_value()
    while True:
        value_2 = second_value()
        print(value_1)
        print(value_2)
        print(logo)
        print(f"Compare A: {value_1[0]}")
        print(vs)
        print(f"Against B: {value_2[0]}")
        value_1_followers=value_1[1]
        value_2_followers=value_2[1]
        user_input=input(f"Who has more followers? Type 'A' or 'B': ").lower()
        if user_input == 'a':
            if value_1_followers > value_2_followers:
                user_score+=1
                print(f"You're Right. Current Score {user_score}")
                value_1 = value_2
            else:
                print(f"Sorry That's wrong. Final score {user_score}")
                break
        elif user_input == 'b':
                if value_2_followers > value_1_followers:
                    user_score+=1
                    print(f"You're Right. Current Score {user_score}")
                    value_2 = value_1
                else:
                    print(f"Sorry That's wrong. Final score {user_score}")
                    break
final_game()
