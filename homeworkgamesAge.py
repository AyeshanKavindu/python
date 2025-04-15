games = [
    {"name": "GTA V", "minimum_age": 18},
    {"name": "Ludo", "minimum_age": 7},
    {"name": "Call of Duty", "minimum_age": 17},
    {"name": "Free Fire", "minimum_age": 16}
]


def check_game_age(game_age, user_age):
    return user_age >= game_age


user_age = int(input("Please enter your age: "))

for game in games:
    if check_game_age(game["minimum_age"], user_age):
        print(f"You can play {game['name']}.")
    else:
        print(f"You cannot play {game['name']}.")
