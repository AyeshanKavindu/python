game_list = [
    {"game_name": "Free Fire", "game_editor": "Ayeshan", "game_year": "2020"}
]

new_game = {
    "game_name": input("Enter a game name: "),
    "game_editor": input("Enter editor name: "),
    "game_year": input("Enter the game year: ")
}

game_list.append(new_game)

for game in game_list:
    print("Game Name:", game["game_name"])
    print("Editor:", game["game_editor"])
    print("Year:", game["game_year"])
    print("")
