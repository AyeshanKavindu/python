games = []

while True:
   u_games = input("Enter your game (or type 'enter' to stop): ")
   
   if u_games == "":
       break
   else:
       games.append(u_games)

for game in games:
 print(games)     
